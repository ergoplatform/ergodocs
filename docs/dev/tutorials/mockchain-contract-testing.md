---
tags:
  - fleet-sdk
  - mock-chain
  - typescript
  - ergoscript
  - testing
  - smart-contracts
  - vitest
  - tutorial
owner: docs
last_reviewed: 2026-11-21
---

# Testing Smart Contracts with MockChain

`@fleet-sdk/mock-chain` lets you compile ErgoScript contracts, construct off-chain transactions, and verify both happy-path execution and adversarial failure cases locally in TypeScript without deploying to Testnet or running a full node.

By the end of this tutorial, you will set up a repeatable [Vitest](https://vitest.dev/) test suite that validates:

1. Multi-party signature and block-height conditions (`HEIGHT > refundDeadline`).
2. Stateful self-replicating eUTXO covenants that conserve tokens and storage-rent reserves across partial purchases.
3. Adversarial security checks (`{ throw: false }`), including defense against eUTXO double-satisfaction attacks.

## Prerequisites

- **Node.js** `>= 18` and `npm`
- Basic familiarity with [ErgoScript](ergoscript.md) box registers (`R4`–`R9`) and [Fleet SDK](fleet.md) transaction builders

## 1. Initialize the Test Project

Create a fresh TypeScript project and install the Fleet SDK packages alongside `vitest`:

```bash
mkdir ergo-mockchain-tests && cd ergo-mockchain-tests
npm init -y
npm pkg set type="module" scripts.test="vitest run"
npm install -D typescript vitest @fleet-sdk/core @fleet-sdk/compiler @fleet-sdk/mock-chain
```

Create a minimal `tsconfig.json`:

```json
{
  "compilerOptions": {
    "target": "ESNext",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "strict": true,
    "skipLibCheck": true
  }
}
```

## 2. Test a Multi-Party Escrow Contract with Timeouts

Create `tests/escrowDepositContract.spec.ts`. In Ergo, multi-party spending paths compose naturally with Sigma propositions (`&&` and `||`), while `mockChain.jumpTo(height)` lets you test block-height transitions deterministically.

Notice two practices in the contract below:

- Named constants (`buyerPK`, `sellerPK`, `arbiterPK`, `refundDeadline`, `maxMinerFee`) are injected safely at compile time through `compile(..., { map })` rather than string interpolation.
- In dispute branches (`sellerAward` and `buyerAward`), the script verifies `OUTPUTS(0).propositionBytes == sellerPK.propBytes` so a co-signing arbiter cannot divert funds to an unintended address.

```typescript
import { MockChain } from "@fleet-sdk/mock-chain";
import { compile } from "@fleet-sdk/compiler";
import {
  OutputBuilder,
  SGroupElement,
  SInt,
  SLong,
  SSigmaProp,
  TransactionBuilder
} from "@fleet-sdk/core";
import { afterEach, describe, expect, it } from "vitest";

const ESCROW_DEPOSIT = 5_000_000_000n; // 5 ERG
const MAX_MINER_FEE = 1_100_000n; // 0.0011 ERG

const ESCROW_DEPOSIT_SCRIPT = `{
  val cooperativeRelease = buyerPK && sellerPK

  val sellerAward =
    arbiterPK &&
    sellerPK &&
    sigmaProp(
      OUTPUTS.size >= 1 &&
      OUTPUTS(0).propositionBytes == sellerPK.propBytes &&
      OUTPUTS(0).value >= SELF.value - maxMinerFee
    )

  val buyerAward =
    arbiterPK &&
    buyerPK &&
    sigmaProp(
      OUTPUTS.size >= 1 &&
      OUTPUTS(0).propositionBytes == buyerPK.propBytes &&
      OUTPUTS(0).value >= SELF.value - maxMinerFee
    )

  val timeoutRefund = buyerPK && sigmaProp(HEIGHT > refundDeadline)

  cooperativeRelease || sellerAward || buyerAward || timeoutRefund
}`;

describe("Arbiter escrow deposit contract", () => {
  const mockChain = new MockChain({ height: 1_052_944 });
  const refundDeadline = mockChain.height + 720;

  const buyer = mockChain.newParty("Buyer");
  const seller = mockChain.newParty("Seller");
  const arbiter = mockChain.newParty("Arbiter");

  const ergoTree = compile(ESCROW_DEPOSIT_SCRIPT, {
    map: {
      buyerPK: SSigmaProp(SGroupElement(buyer.key.publicKey)),
      sellerPK: SSigmaProp(SGroupElement(seller.key.publicKey)),
      arbiterPK: SSigmaProp(SGroupElement(arbiter.key.publicKey)),
      refundDeadline: SInt(refundDeadline),
      maxMinerFee: SLong(MAX_MINER_FEE)
    }
  });

  const escrowContract = mockChain.addParty(ergoTree.toHex(), "Escrow Deposit Contract");

  afterEach(() => {
    mockChain.reset();
  });

  it("Should allow cooperative release co-signed by Buyer and Seller", () => {
    escrowContract.addBalance({ nanoergs: ESCROW_DEPOSIT });

    const payout = ESCROW_DEPOSIT - MAX_MINER_FEE;
    const transaction = new TransactionBuilder(mockChain.height)
      .from(escrowContract.utxos)
      .to(new OutputBuilder(payout, seller.address))
      .payMinFee()
      .build();

    expect(mockChain.execute(transaction, { signers: [buyer, seller] })).to.be.true;
    expect(seller.balance).to.be.deep.equal({ nanoergs: payout, tokens: [] });
  });

  it("Should reject an Arbiter and Seller spend that diverts funds to Arbiter", () => {
    escrowContract.addBalance({ nanoergs: ESCROW_DEPOSIT });

    const payout = ESCROW_DEPOSIT - MAX_MINER_FEE;
    const transaction = new TransactionBuilder(mockChain.height)
      .from(escrowContract.utxos)
      .to(new OutputBuilder(payout, arbiter.address))
      .payMinFee()
      .build();

    expect(
      mockChain.execute(transaction, { signers: [arbiter, seller], throw: false })
    ).to.be.false;
    expect(escrowContract.balance).to.be.deep.equal({ nanoergs: ESCROW_DEPOSIT, tokens: [] });
  });

  it("Should reject a unilateral refund by Buyer before the deadline", () => {
    escrowContract.addBalance({ nanoergs: ESCROW_DEPOSIT });

    const payout = ESCROW_DEPOSIT - MAX_MINER_FEE;
    const transaction = new TransactionBuilder(mockChain.height)
      .from(escrowContract.utxos)
      .to(new OutputBuilder(payout, buyer.address))
      .payMinFee()
      .build();

    expect(mockChain.execute(transaction, { signers: [buyer], throw: false })).to.be.false;
    expect(escrowContract.balance).to.be.deep.equal({ nanoergs: ESCROW_DEPOSIT, tokens: [] });
  });

  it("Should allow Buyer to reclaim funds unilaterally after the deadline expires", () => {
    escrowContract.addBalance({ nanoergs: ESCROW_DEPOSIT });
    mockChain.jumpTo(refundDeadline + 1);

    const payout = ESCROW_DEPOSIT - MAX_MINER_FEE;
    const transaction = new TransactionBuilder(mockChain.height)
      .from(escrowContract.utxos)
      .to(new OutputBuilder(payout, buyer.address))
      .payMinFee()
      .build();

    expect(mockChain.execute(transaction, { signers: [buyer] })).to.be.true;
    expect(buyer.balance).to.be.deep.equal({ nanoergs: payout, tokens: [] });
  });
});
```

## 3. Test Stateful Covenants and Double-Satisfaction Defenses

Many Ergo protocols use **self-replicating boxes** that allow anyone to purchase a slice of tokens as long as a continuation box preserves the remaining token supply and minimum nanoERG reserve.

When writing and testing open-order or pool contracts in the eUTXO model, always test against **double-satisfaction**: if two contract boxes are spent in the same transaction and both merely check that `OUTPUTS(0)` pays `sellerPK`, an attacker can spend two boxes while paying the seller only once. Binding `OUTPUTS(0).R4[Coll[Byte]].getOrElse(Coll[Byte]()) == SELF.id` ties the seller payout box to a single unique input box ID.

Create `tests/selfReplicatingTokenSaleContract.spec.ts`:

```typescript
import { MockChain } from "@fleet-sdk/mock-chain";
import { compile } from "@fleet-sdk/compiler";
import {
  OutputBuilder,
  SByte,
  SColl,
  SGroupElement,
  SLong,
  SSigmaProp,
  TransactionBuilder
} from "@fleet-sdk/core";
import { afterEach, describe, expect, it } from "vitest";

const SALE_TOKEN_ID = "1111111111111111111111111111111111111111111111111111111111111111";
const MIN_BOX_VALUE = 1_000_000n;
const PRICE_PER_TOKEN = 10_000_000n; // 0.01 ERG per token

function hexToBytes(hexString: string): Uint8Array {
  return Uint8Array.from({ length: hexString.length / 2 }, (_, index) =>
    Number.parseInt(hexString.slice(index * 2, index * 2 + 2), 16)
  );
}

const SELF_REPLICATING_TOKEN_SALE_SCRIPT = `{
  val saleCycleValid = if (OUTPUTS.size >= 1) {
    val selfTokenId = SELF.tokens(0)._1
    val selfTokenAmount = SELF.tokens(0)._2

    val remainingTokens = if (
      OUTPUTS.size >= 2 &&
      OUTPUTS(1).propositionBytes == SELF.propositionBytes &&
      OUTPUTS(1).tokens.size == 1 &&
      OUTPUTS(1).tokens(0)._1 == selfTokenId
    ) {
      OUTPUTS(1).tokens(0)._2
    } else {
      0L
    }

    val continuationSafe = remainingTokens == 0L || OUTPUTS(1).value >= SELF.value
    val soldTokens = selfTokenAmount - remainingTokens

    val payoutValid =
      soldTokens > 0L &&
      OUTPUTS(0).propositionBytes == sellerPK.propBytes &&
      OUTPUTS(0).value >= soldTokens * pricePerToken &&
      OUTPUTS(0).R4[Coll[Byte]].getOrElse(Coll[Byte]()) == SELF.id

    continuationSafe && payoutValid
  } else {
    false
  }

  sellerPK || sigmaProp(saleCycleValid)
}`;

describe("Self-replicating token sale contract", () => {
  const mockChain = new MockChain({ height: 1_052_944 });

  const seller = mockChain.newParty("Seller");
  const buyer = mockChain.newParty("Buyer");
  const attacker = mockChain.newParty("Attacker");

  const ergoTree = compile(SELF_REPLICATING_TOKEN_SALE_SCRIPT, {
    map: {
      sellerPK: SSigmaProp(SGroupElement(seller.key.publicKey)),
      pricePerToken: SLong(PRICE_PER_TOKEN)
    }
  });

  const saleContract = mockChain.addParty(ergoTree.toHex(), "Token Sale Contract");

  afterEach(() => {
    mockChain.reset();
  });

  it("Should allow a partial purchase when continuation box preserves remaining supply", () => {
    saleContract.addBalance({
      nanoergs: MIN_BOX_VALUE,
      tokens: [{ tokenId: SALE_TOKEN_ID, amount: 100n }]
    });
    buyer.addBalance({ nanoergs: 2_000_000_000n });

    const saleBox = saleContract.utxos.toArray()[0];
    const tokensToBuy = 25n;
    const remainingTokens = 75n;
    const sellerPayout = tokensToBuy * PRICE_PER_TOKEN;

    const transaction = new TransactionBuilder(mockChain.height)
      .from([saleBox, ...buyer.utxos.toArray()])
      .to([
        new OutputBuilder(sellerPayout, seller.address).setAdditionalRegisters({
          R4: SColl(SByte, hexToBytes(saleBox.boxId)).toHex()
        }),
        new OutputBuilder(MIN_BOX_VALUE, saleContract.address).addTokens({
          tokenId: SALE_TOKEN_ID,
          amount: remainingTokens
        }),
        new OutputBuilder(MIN_BOX_VALUE, buyer.address).addTokens({
          tokenId: SALE_TOKEN_ID,
          amount: tokensToBuy
        })
      ])
      .sendChangeTo(buyer.address)
      .payMinFee()
      .build();

    expect(mockChain.execute(transaction, { signers: [buyer] })).to.be.true;
    expect(saleContract.balance).to.be.deep.equal({
      nanoergs: MIN_BOX_VALUE,
      tokens: [{ tokenId: SALE_TOKEN_ID, amount: remainingTokens }]
    });
  });

  it("Should reject a double-satisfaction attack across two concurrent sale boxes", () => {
    saleContract.addBalance({
      nanoergs: MIN_BOX_VALUE,
      tokens: [{ tokenId: SALE_TOKEN_ID, amount: 10n }]
    });
    saleContract.addBalance({
      nanoergs: MIN_BOX_VALUE,
      tokens: [{ tokenId: SALE_TOKEN_ID, amount: 10n }]
    });
    attacker.addBalance({ nanoergs: 2_000_000_000n });

    const [firstSaleBox, secondSaleBox] = saleContract.utxos.toArray();
    const singleBoxPayout = 10n * PRICE_PER_TOKEN;

    const transaction = new TransactionBuilder(mockChain.height)
      .from([firstSaleBox, secondSaleBox, ...attacker.utxos.toArray()])
      .to([
        new OutputBuilder(singleBoxPayout, seller.address).setAdditionalRegisters({
          R4: SColl(SByte, hexToBytes(firstSaleBox.boxId)).toHex()
        }),
        new OutputBuilder(MIN_BOX_VALUE, attacker.address).addTokens({
          tokenId: SALE_TOKEN_ID,
          amount: 20n
        })
      ])
      .sendChangeTo(attacker.address)
      .payMinFee()
      .build();

    expect(mockChain.execute(transaction, { signers: [attacker], throw: false })).to.be.false;
  });
});
```

## 4. Run the Suite

Execute Vitest from the project root:

```bash
npm test
```

All happy-path and adversarial cases run in memory through the Sigma interpreter embedded in `@fleet-sdk/mock-chain` without external network calls.

## Troubleshooting Common Pitfalls

| Symptom | Root Cause | Fix |
| --- | --- | --- |
| `Option.get` evaluation failure on missing register | Calling `OUTPUTS(0).R4[Coll[Byte]].get` when `R4` is empty or holds another type | Use `.getOrElse(Coll[Byte]())` with a safe sentinel value instead of `.get` |
| Boundary height off-by-one during `mockChain.execute()` | `mockBlockchainStateContext()` sets `sigmaPreHeader` one block ahead of `sigmaLastHeaders`, and `mockChain.reset()` clears UTxOs without rewinding `mockChain.height` | Explicitly call `mockChain.jumpTo(targetHeight)` in height-sensitive tests and account for candidate block height |
| `SColl(SByte, ...)` rejects a hex string or undefined helper | `SColl(SByte, data)` expects a `Uint8Array` (or byte array) | Convert 32-byte hex IDs (such as `boxId` or `tokenId`) to `Uint8Array` before passing to `SColl(SByte, ...)` |
| Contract input omitted from built transaction | `TransactionBuilder.from()` skips inputs not needed to cover output asset totals | Pass `.from(contractBox, { ensureInclusion: true })` when the contract box carries no unique required asset |
| Test throws instead of returning `false` on invalid spend | `mockChain.execute()` throws script-reduction errors by default for debugging | Pass `{ throw: false }` when asserting that an unauthorized spend is rejected |

## Related Documentation

- [Fleet SDK](fleet.md)
- [Fleet SDK Recipes](fleet-sdk-recipes.md)
- [Chained Transactions](chained-tx.md)
- [ErgoScript](ergoscript.md)
- [fleet-by-example](https://github.com/fleet-sdk/fleet-by-example)
