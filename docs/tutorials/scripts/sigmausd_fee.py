#!/usr/bin/env python3
import argparse
import csv
import datetime as dt
import json
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

NANOERG = 1_000_000_000


def fetch_json(url: str, timeout_s: int, retries: int, backoff_s: float) -> dict:
    last_err = None
    for attempt in range(retries):
        try:
            req = Request(
                url,
                headers={
                    "Accept": "application/json",
                    "User-Agent": "sigmausd-fee-audit/1.1",
                },
            )
            with urlopen(req, timeout=timeout_s) as resp:
                raw = resp.read()
            return json.loads(raw.decode("utf-8"))
        except HTTPError as e:
            last_err = e
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(backoff_s * (2**attempt))
                continue
            raise
        except URLError as e:
            last_err = e
            time.sleep(backoff_s * (2**attempt))
            continue
        except Exception as e:
            last_err = e
            time.sleep(backoff_s * (2**attempt))
            continue
    raise RuntimeError(f"Fetch failed after {retries} tries: {url}\nLast error: {last_err}")


def iso_utc_from_ms(ms: int) -> str:
    try:
        return (
            dt.datetime.utcfromtimestamp(ms / 1000)
            .replace(tzinfo=dt.timezone.utc)
            .isoformat()
        )
    except Exception:
        return ""


def iter_tx_ids(
    api_base: str,
    address: str,
    page_limit: int,
    sleep_s: float,
    timeout_s: int,
    retries: int,
    backoff_s: float,
):
    offset = 0
    total = None

    while True:
        url = f"{api_base}/addresses/{address}/transactions?offset={offset}&limit={page_limit}"
        data = fetch_json(url, timeout_s=timeout_s, retries=retries, backoff_s=backoff_s)

        if total is None and isinstance(data.get("total"), int):
            total = data["total"]

        items = data.get("items") or []
        if not items:
            return

        for it in items:
            tx_id = it.get("id") or it.get("txId")
            if tx_id:
                yield tx_id

        offset += len(items)

        if isinstance(total, int) and offset >= total:
            return

        time.sleep(sleep_s)


def analyze_tx(tx: dict, address: str, seed_value: int) -> dict:
    inputs = tx.get("inputs") or []
    outputs = tx.get("outputs") or []

    ins_addr = [i for i in inputs if i.get("address") == address and isinstance(i.get("value"), int)]
    outs_addr = [o for o in outputs if o.get("address") == address and isinstance(o.get("value"), int)]

    big_ins = [i for i in ins_addr if i["value"] >= seed_value]
    big_outs = [o for o in outs_addr if o["value"] >= seed_value]

    in_sum = sum(i["value"] for i in ins_addr)
    out_sum = sum(o["value"] for o in outs_addr)

    exact_sum = 0
    exact_count = 0
    for o in outs_addr:
        if o["value"] == seed_value:
            exact_sum += o["value"]
            exact_count += 1

    delta_event = 0
    if big_ins and big_outs:
        vin = sum(i["value"] for i in big_ins)
        vout = sum(o["value"] for o in big_outs)
        d = vout - vin
        if d > 0:
            delta_event = d

    return {
        "tx_id": tx.get("id"),
        "height": tx.get("inclusionHeight"),
        "timestamp_ms": tx.get("timestamp"),
        "timestamp_iso": iso_utc_from_ms(tx.get("timestamp", 0)) if isinstance(tx.get("timestamp"), int) else "",
        "delta_event": delta_event,
        "exact_sum": exact_sum,
        "exact_count": exact_count,
        "in_sum": in_sum,
        "out_sum": out_sum,
    }


def main() -> int:
    p = argparse.ArgumentParser(description="Audit SigmaUSD provider fees for an Ergo address.")
    p.add_argument(
        "--address",
        default="9hFmeUHVttZmgtq4DEosEzJb3bTjx9HMJVptmMgfaHH9tYyGYTE",
        help="Provider address to scan",
    )
    p.add_argument(
        "--seed-value",
        type=int,
        default=100_622_500_000,
        help="NanoERG marker (Dmitry: 100622500000)",
    )
    p.add_argument(
        "--api-base",
        default="https://api.ergoplatform.com/api/v1",
        help="Explorer API base",
    )
    p.add_argument("--page-limit", type=int, default=500, help="Max 500")
    p.add_argument("--sleep", type=float, default=0.15, help="Sleep between page and tx calls")
    p.add_argument("--timeout", type=int, default=30, help="HTTP timeout seconds")
    p.add_argument("--retries", type=int, default=6, help="Retry count")
    p.add_argument("--backoff", type=float, default=0.5, help="Backoff base seconds")
    p.add_argument("--max-txs", type=int, default=0, help="0 means no limit")
    p.add_argument("--csv", default="sigmausd_fee_events.csv", help="CSV output path")
    args = p.parse_args()

    total_delta = 0
    total_exact = 0
    total_exact_count = 0
    total_in = 0
    total_out = 0

    rows = []
    scanned = 0

    for tx_id in iter_tx_ids(
        api_base=args.api_base,
        address=args.address,
        page_limit=args.page_limit,
        sleep_s=args.sleep,
        timeout_s=args.timeout,
        retries=args.retries,
        backoff_s=args.backoff,
    ):
        tx = fetch_json(
            f"{args.api_base}/transactions/{tx_id}",
            timeout_s=args.timeout,
            retries=args.retries,
            backoff_s=args.backoff,
        )

        m = analyze_tx(tx, address=args.address, seed_value=args.seed_value)

        scanned += 1
        total_delta += m["delta_event"]
        total_exact += m["exact_sum"]
        total_exact_count += m["exact_count"]
        total_in += m["in_sum"]
        total_out += m["out_sum"]

        if m["delta_event"] > 0 or m["exact_count"] > 0:
            rows.append(m)

        if scanned % 200 == 0:
            print(f"txs_scanned={scanned} delta_fee_erg={total_delta / NANOERG:.9f}")

        if args.max_txs and scanned >= args.max_txs:
            break

        time.sleep(args.sleep)

    with open(args.csv, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "tx_id",
                "height",
                "timestamp_ms",
                "timestamp_iso",
                "delta_event",
                "exact_sum",
                "exact_count",
                "in_sum",
                "out_sum",
            ],
        )
        w.writeheader()
        w.writerows(rows)

    net = total_in - total_out

    print(f"address={args.address}")
    print(f"seed_value={args.seed_value}")
    print(f"txs_scanned={scanned}")
    print(f"delta_fee_erg={total_delta / NANOERG:.9f}")
    print(f"exact_value_erg={total_exact / NANOERG:.9f} exact_count={total_exact_count}")
    print(f"net_inflow_erg={net / NANOERG:.9f} inflow_erg={total_in / NANOERG:.9f} outflow_erg={total_out / NANOERG:.9f}")
    print(f"events_csv={args.csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
