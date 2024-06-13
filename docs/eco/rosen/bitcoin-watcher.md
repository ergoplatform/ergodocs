# Bitcoin Rosen Bridge Watcher Setup

/// details | IMPORTANT
     {type: warning, open: true}
**IMPORTANT**: Update all of your Watcher services before 18 JUN, 12 AM UTC by using the following from the Watcher directory:

docker compose down
docker compose pull
docker compose up -d

A breaking change has been implemented in this version. We will continue to support older versions until 18 JUN, 12 AM UTC.

Please update your Watcher service as soon as possible, if you don't update your watcher before that time, your permits may be considered fraudulent, and you will lose them!

Please reach out on Telegram or Discord if you require assistance.
///

Watchers are integral to the Rosen Bridge, serving as cross-chain oracles. They observe and report deposit events on the Bitcoin network to Ergo, contributing to the network's security and expansion.

## Watcher Setup Guides

//// details | Tutorials
     {type: info, open: true}
/// details | Pre-requisites
     {type: danger, open: true}
Before setting up a Bitcoin Watcher, ensure you meet the following requirements:

- A machine with the recommended specs:
  - 8GB+ RAM
  - 1TB+ storage if running a Bitcoin full node. 30GB otherwise for the Ergo Node. 
  - 2+ CPU cores
  - Reliable always-on internet connection (watcher must maintain 95%+ uptime)
- [Docker and Docker Compose installed](https://docs.docker.com/get-docker/)
- Basic command line knowledge
- (Recommended) An [Ergo node synced](install.md) on your machine
- (Optional) [Bitcoin Core full node synced](#setting-up-a-bitcoin-node-optional) on your machine
- 800 ERG and 33,000.001 RSN for watcher collateral:
  - [Acquire ERG](https://ergoplatform.org/en/exchanges/)
  - [Acquire RSN](https://spectrum.fi/)
///

There is a [General Watchers app Tutorials Playlist](https://youtube.com/playlist?list=PLyQeADPK2PWgztdc9lCvAyqjknPaN9woQ&si=SNYxoZMv2iID610o), and more tailored guides for each platform will be available soon.

/// details | Windows
     {type: info, open: false}
A step-by-step guide for setting up a Bitcoin Watcher on Windows will be available soon.
///

/// details | Mac
     {type: info, open: false}
A step-by-step guide for setting up a Bitcoin Watcher on Mac will be available soon.
///

/// details | Linux
     {type: info, open: false}
A step-by-step guide for setting up a Bitcoin Watcher on Linux will be available soon.
///
////

Below you'll find a step-by-step guide to [setting up a Bitcoin Watcher](#setting-up-the-watcher), as well as [frequently asked questions](#watcher-faqs) and [troubleshooting tips](#troubleshooting).

## Setting Up a Bitcoin Node (Optional)

For optimal watcher performance and decentralization, it's recommended to run your own fully synced Bitcoin node. However this will consume significant disk space so alternatively you can use a public node as detailed in the next section. 

1. Install Bitcoin Core following the [official instructions](https://bitcoin.org/en/download) for your OS.

2. Configure Bitcoin Core:
   - Locate the `bitcoin.conf` file in the Bitcoin data directory:
     - Linux: `~/.bitcoin/`
     - macOS: `~/Library/Application Support/Bitcoin/`
     - Windows: `%APPDATA%\Bitcoin\`
   - Open `bitcoin.conf` with a text editor or create it if it doesn't exist.

3. Generate an RPC username and password:
   - Visit [this RPC auth generator](https://jlopp.github.io/bitcoin-core-rpc-auth-generator)
   - Enter a username and click "Generate"
   - Copy the generated line starting with `rpcauth=`

4. Edit `bitcoin.conf` to enable the RPC server and allow the watcher to connect:
   - Paste the `rpcauth` line you copied
   - Add the following lines to enable the RPC server:
     ```
     server=1
     rpcbind=0.0.0.0
     rpcallowip=0.0.0.0/0
     txindex=1
     rest=1
     ```
   - To limit RPC access to only the watcher container, set `rpcallowip` to the Docker network range:
     ```
     rpcallowip=172.16.0.0/12
     ```

   - Save the file

5. If `bitcoind` was already running, stop and restart it:
   ```
   bitcoin-cli stop
   bitcoind -daemon
   ```

6. Verify the node is running and wait for it to sync:
   ```
   bitcoin-cli getblockchaininfo
   ```
   Look for `"initialblockdownload": false` to confirm the node is synced.

Your Bitcoin node is now ready to support your watcher. Proceed with watcher setup.

/// details | Running a Pruned Bitcoin Node
     {type: danger, open: false}
A pruned Bitcoin node is not compatible with the Rosen Bitcoin bridge watcher. The watcher requires the `txindex=1` setting, which is not supported by pruned nodes. If you initially synced a pruned node, you'll need to restart the sync with a full node.
///

## Setting Up the Watcher

1. Choose a directory for your Bitcoin watcher (e.g., `~/watchers/btc`) and create it:
   ```
   mkdir -p ~/watchers/btc
   cd ~/watchers/btc
   ```

2. Create a `local.yaml` file with the watcher configuration:
   ```yaml
   network: 'bitcoin'
   ergo:
     type: 'explorer'
     initialHeight: 1284340 
     node:
       url: 'https://node.ergopool.io/'
   bitcoin:
     type: 'rpc'
     rpc:
       url: 'http://<user>:<password>@localhost:8332'
     initial:
       height: 847480
   observation:
     confirmation: 2
     validThreshold: 72
   ```
   - Replace `<user>` and `<password>` with the RPC username and password from your `bitcoin.conf`.
   - The `initialHeight` settings determine the starting block height for scanning. Set these to recent blocks to speed up initial sync. Find the current Ergo height at [explorer.ergoplatform.com](https://explorer.ergoplatform.com/) and Bitcoin height at [mempool.space](https://mempool.space).
   - If using an external Bitcoin RPC provider instead of your own node, replace the `bitcoin` section with:
     ```yaml
     bitcoin:
       type: 'esplora'
       esplora:
         url: 'https://mempool.space'
         timeout: 60000
       initial:
         height: 847480
     ```

- If you would like to use a different source than mempool, replace `https://mempool.space` with the base URL of your chosen API provider.
- Adjust the timeout value (in milliseconds) if needed. This is how long the watcher will wait for a response from the API before timing out.
- Set `initial.height` to a recent Bitcoin block height to minimize the number of blocks the watcher needs to scan during initial sync. You can find the current block height on a Bitcoin explorer like mempool.space.

3. Save the `local.yaml` file and start your watcher as described in the main setup guide:

   ```bash
   docker compose up -d
   ```

   The watcher will now use the specified public Bitcoin API instead of a local node.

Note that public API providers may have rate limits, which could slow down your watcher's syncing speed. If you encounter frequent rate limiting errors, consider upgrading to a paid plan or switching to a different provider.

Also, keep in mind that using a public API makes your watcher dependent on a third-party service. If the API goes down or becomes unreliable, it will affect your watcher's performance. Running your own Bitcoin node, while more resource-intensive, gives you maximum reliability and privacy.



4. Create a `docker-compose.yml` file to define the watcher service:
   ```yaml
   version: '3.7'

   services:
     service:
       image: rosen/watcher:3.0.0
       container_name: watcher_btc
       volumes:
         - ./local.yaml:/app/services/watcher/config/local.yaml
         - ./data:/app/services/watcher/data
       ports:
         - 3030:3030
       environment:
         NODE_ENV: ${NODE_ENV:-production}
       restart: unless-stopped
       logging:
         driver: "json-file"
         options:
           max-size: "10m"
           max-file: "5"
       networks:
         - rosen

   volumes:
     data:

   networks:
     rosen:
       name: rosen_default
   ```
   - If setting up multiple watchers on the same machine, change `container_name` and the host port in `ports` to avoid conflicts.
   - The `networks` section allows the watcher to communicate with other Rosen containers on the same machine over the `rosen_default` Docker network.

5. Create a `.env` file to set environment variables:
   ```
   CURRENT_NETWORK=BITCOIN
   DATABASE_URL=file:/app/services/watcher/data/database/data.sqlite
   HTTP_PORT=3030
   LOGGER_LEVEL=info
   ```
   - If running multiple watchers, ensure `HTTP_PORT` is unique for each.

6. Start the watcher:
   ```
   docker compose up -d
   ```
   Docker will download the watcher image and start the container.

7. Check the logs to monitor sync progress:
   ```
   docker compose logs -f service
   ```
   You should see log entries indicating the watcher is scanning blocks. Initial sync may take several hours depending on your `initial` height settings. Check percentage synced with:
   ```
   curl http://localhost:3030/api/status | jq '.result.scanner."bitcoin-rpc".progress'
   ```

8. Once sync reaches the chain tip, access the watcher's web interface at `http://localhost:3030` (or the configured port).

9. Use the web interface to lock your watcher collateral (800 ERG and 33,000.001 RSN), registering your watcher with the bridge.
   - If you encounter an insufficient funds error, check that your wallet has exactly the required amounts. The `/api/collateral` endpoint can provide the precise values.
   - After locking collateral, verify it shows as locked in the web interface and via the `/api/collateral` endpoint.

Your Bitcoin watcher is now set up and securing the Rosen bridge. Monitor the logs (`docker compose logs -f service`) to ensure your watcher remains synced.

## Updating the Watcher

Watcher updates are periodically required, especially before network upgrades. Update announcements are posted in the [Rosen Telegram](https://t.me/rosenbridge_erg) and [Discord](https://discord.gg/nhYh832X7P).

To update:

1. Navigate to your watcher directory and pull the latest image:
   ```
   cd ~/watchers/btc
   docker compose pull
   ```

2. Recreate the watcher container with the new image:
   ```
   docker compose up -d
   ```

3. Check the logs to ensure the watcher started successfully:
   ```
   docker compose logs -f service
   ```

4. Verify in the web interface that the watcher version is the latest required.



## Interacting with a Headless Server

/// details | Interacting with a headless server
     {type: info, open: false}
To interact with a headless server, you can use SSH (Secure Shell) to establish a secure connection. You can also forward ports to access specific services on the server. In the example below, we are using SSH to forward the local port 3030 to port 3030 on the server. This allows us to access a service running on port 3030 of the server as if it was running on our local machine.

```bash
ssh -L 3030:127.0.0.1:3030 user@watcher-server
```

In this command:

- `ssh` is the command to start the SSH client program.
- `-L 3030:127.0.0.1:3030` specifies that the local port 3030 should be forwarded to port 3030 on the server. `127.0.0.1` is the loopback IP address, which refers to the server itself in this context.
- `user@watcher-server` specifies the username and the server to connect to. Replace `user` with your actual username and `watcher-server` with the actual hostname or IP address of your server.
///






## Tips

/// details | Security Considerations
     {type: warning, open: false}

Keep your watcher machine and Docker install updated with the latest security patches.
Don't reuse your watcher's RPC password anywhere else.
Secure your machine's SSH login with a strong password and/or public key authentication.
Consider running the watcher in a dedicated VM or container for isolation.
Regularly monitor your watcher's logs and web UI for any signs of issues.
Keep your collateral wallet secure, as the wallet owner has control over unstaking collateral.
///

/// details | Monitoring and Alerting
     {type: info, open: false}
Maintaining high watcher uptime is critical to avoid collateral penalties. Consider setting up external monitoring and alerting:

Services like Uptime Robot or Pingdom can monitor your watcher's web UI and alert you if it goes down.
Use a service like Healthchecks.io to monitor your watcher's log for error keywords and send alerts.
The Rosen team's monitoring will alert in Telegram/Discord if your watcher is down, but additional self-monitoring is strongly recommended.
///

/// details | Increasing Bitcoin Node DbCache
     {type: info, open: false}
To speed up the initial sync of your Bitcoin node, you can increase the dbcache setting if you have sufficient RAM. For example, to allocate 4GB of cache, add the following line to your bitcoin.conf:
```
dbcache=4096
```

Adjust the value based on your available memory.
///
/// details | Current Bitcoin Blockchain Size
     {type: info, open: false}
As of June 2024, the Bitcoin blockchain size is approximately 657GB. Keep this in mind when provisioning storage for your Bitcoin node.
///
/// details | Bitcoin Blockchain Snapshots
There are services that provide Bitcoin blockchain snapshots to speed up the initial sync process. However, be cautious when using these snapshots, as they may not be compatible with the txindex=1 requirement for the Rosen Bitcoin watcher. Ensure that the snapshot is from a full node with transaction indexing enabled.
///


/// details | Monitoring Bitcoin Node Sync Progress
     {type: info, open: false}
You can monitor the sync progress of your Bitcoin node using the `bitcoin-cli` command:

```bash
bitcoin-cli getblockchaininfo
```

Look for the `"verificationprogress"` field in the output. A value of `1.000000` indicates that the node is fully synced.
///

/// details | Using a Separate Machine for the Bitcoin Node
     {type: info, open: false}
If you have limited resources on your watcher machine, consider running the Bitcoin node on a separate machine. This way, the resource-intensive block syncing process won't affect the performance of your watcher.

In this case, update the `rpc.url` in your watcher's `local.yaml` to point to the remote Bitcoin node's IP address and RPC port:

```yaml
bitcoin:
  type: 'rpc'
  rpc:
    url: 'http://<user>:<password>@<remote-ip>:8332'
```

Make sure to configure the Bitcoin node's `rpcallowip` setting to allow connections from the watcher machine's IP.
///

/// details | Enabling Transaction Broadcasting
     {type: info, open: false}
If you want your Bitcoin node to be able to broadcast transactions (not required for the watcher but useful for debugging), make sure the following line is added to your `bitcoin.conf`:

```
zmqpubrawtx=tcp://0.0.0.0:28332
```

This enables the ZeroMQ raw transaction broadcasting feature.
///

/// details | Using a Config File for Environment Variables
     {type: info, open: false}
Instead of specifying environment variables in the `docker-compose.yml` file, you can use a separate `.env` file. This keeps your compose file cleaner and allows for easier management of environment variables.

Create a `.env` file in the same directory as your `docker-compose.yml` with the following content:

```
CURRENT_NETWORK=BITCOIN
DATABASE_URL=file:/app/services/watcher/data/database/data.sqlite
HTTP_PORT=3030
LOGGER_LEVEL=info
```

Update your `docker-compose.yml` to reference these variables:

```yaml
services:
  service:
    image: rosen/watcher:3.0.0
    container_name: watcher_btc
    env_file:
      - .env
    # ... rest of the service definition
```

Docker Compose will automatically load the variables from the `.env` file.
///




## Troubleshooting

### UI Errors

/// details | scanner is out of sync
     {type: danger, open: false}
Your scanner is out of sync. You need to wait until it scans all blocks. The service runs every 3 minutes or so. Depending on when it calls and blocks produced, it may drop a block sync here and there but catches up in most cases.

Alternatively, you can delete docker volumes and restart your watcher with a newer initial height. Then it doesn't need to scan as many blocks to be synced.

```bash
docker compose down --volumes
```

Then update the `local.yaml` initial height and rerun the watcher.
///

/// details | Permit Health Broken
     {type: danger, open: false}
By default, the permit health warning parameter is set to 100. This is adjustable locally by adding the following into your `local.yaml` and adjusting as necessary:

```yaml
healthCheck:
  permit:
     warnCommitmentCount: 1 # amount of permits left before giving a warning
     criticalCommitmentCount: 0 # amount of permits left it is critical
```

Adjust the numbers as you wish.

`warnCommitmentCount` will change the warning to yellow when the available Permits reduce to the number.

`criticalCommitmentCount` will change to red when the available Permits reduce to this number.
///

/// details | watcher-db-1 is unhealthy
     {type: danger, open: false}
> dependency failed to start: container watcher-db-1 is unhealthy

- Your `.env` file might be missing? Turn on view file extensions like in the video, are you sure it's `.env` and not `.env.txt`?
- Update your `local.yaml` with the current ergo blockheight.

As a last resort, some users are reporting that this issue can be fixed by pruning existing images and rebuilding:

```bash
docker system prune -a
```

**As long as you don't have other docker images to worry about.**
///

/// details | Lock, Unlock 500 Error
     {type: danger, open: false}
If you're receiving a 500 Error while trying to lock or unlock your ERG and/or RSN, it could possibly be from having an insufficient box value on chain. **This is fixed in the latest release, please update if you have not done so already.**

Update with:
```bash
docker compose pull
docker compose down
docker compose up -d
```

Please check your service logs first. If you see a warning indicating "Box value BoxValue(1100000) is too low, minimum value for box size of ..."

To rectify, add the following to your `local.yaml` in the "ergo:" section with one tab indent (should be the same indent as `initialHeight`):

```yaml
  minBoxValue: '2000000'
```
///

/// details | UnhandeledPromiseRejection
     {type: danger, open: false}
> UnhandeledPromiseRejection, promise rejected with reason Object.....LifeCycle script start failed

There is an issue in ogmios roll backward after a fork. Fix is a work in progress.
///

/// details | The requested image's platform (linux/amd64) does not match the detected host platform
     {type: danger, open: false}
Incompatibility with certain ARM chips in Raspberry Pis and (ARM Mac Mini M1 Asahi Linux: see [this PR](https://github.com/rosen-bridge/operation/issues/6)).
///

### Working with Docker

/// details | Checking logs
     {type: info, open: false}
```bash
docker compose logs
```
///

/// details | Updating your watcher
     {type: info, open: false}
```bash
docker compose pull
docker compose down
docker compose up -d
```
///

/// details | Restarting your watcher
     {type: info, open: false}
You can restart your watcher instance simply by running the following command from within the same folder the `docker-compose.yaml` is stored:

```bash
docker compose up -d
```
///

/// details | no configuration files provided: not found
     {type: danger, open: false}
Check you're in the correct directory. You should be executing `docker compose` commands from within the `operation/watcher` folder.
///

/// details | Dumping databases
     {type: info, open: false}
```bash
docker compose down
docker volume remove watcher_postgres-data
#---edit block height in YAML after this step
docker compose up -d
```
///

/// details | Clearing Volumes
     {type: info, open: false}
You may wish to clear Docker volumes for a number of reasons, e.g., changing `initial.height` to sync. To do so, run the following Docker command from the Watcher directory:

```bash
docker compose down --volumes
```

Re-initiate the Watcher with:

```bash
docker compose up -d
```
///

/// details | Clean Slate
     {type: info, open: false}
If you want to remove everything and start from scratch:

```bash
docker ps -a
docker compose down
docker rm CONTAINERID1 CONTAINERID2 CONTAINERID3
```

Then delete the folder and start fresh.
///



### Operational

/// details | Role and Rewards
     {type: question, open: false}
Watchers are essential for accurate reporting and receive 70% of transaction fees as rewards for successful and accurate reporting (while 30% goes to the guard set). 25% of the emission is also reserved for *'Event-Based Emission (Rewards)'*.
///

/// details | Who can become a Watcher?
     {type: question, open: false}
Anyone. You can actively contribute to the expansion and security audit of the Rosen Bridge by becoming a Watcher. Watchers receive rewards for accurate reporting.

- Configure and run the Watcher app for Bitcoin.
- Top it off with enough RSN and ERG.
- Put in collateral and receive reporting permits.
- Enjoy reporting and getting rewards.
///


/// details | Can I run multiple watchers?
     {type: question, open: false}
Yes, but it incurs financial considerations to prevent abuse. Each instance needs a unique folder and `HTTP_PORT`.
///


/// details | Do I need to do anything after setup?
     {type: question, open: false}
You don't need to manually watch and approve transactions, the software will handle everything automatically, you just need to ensure the watcher keeps running.

1. Observe an event and wait a bit.
2. Create a commitment using report permits.
3. Aggregate all participating watchers commitment (into something called event trigger).
4. Wait for guards stuff, especially target chain tx and reward tx submission.
5. Get rewards.
///

## Watcher FAQs

### Collateral, Permits and Reporting

/// details | Collateral Requirements
     {type: question, open: false}
Each instance requires 800 ERG and 33,000.001 RSN as collateral. This collateral is fully redeemable and the amount is adjustable.
///

/// details | How do I redeem my collateral?
     {type: question, open: false}
You can redeem it after redeeming your last permit token, but if you have unsettled reports, you must wait until those permits are returned.
///

/// details | Permit Acquisition
     {type: question, open: false}
To report, watchers must acquire permits, which are part of the 33,000.001 RSN collateral. Multiple permits are necessary for reporting concurrent events, and permits can be seized if reports are found fraudulent.
///

/// details | Reporting Process
     {type: question, open: false}
- Watchers report deposit events as part of a collective effort.
- A consensus among watchers on an event triggers a final report and guard intervention.
- Guards take necessary actions based on these reports.
- Watchers involved in successful cross-chain settlements are rewarded.
///

/// details | What if my report is successful?
     {type: question, open: false}
You'll receive rewards and your staked amount will be returned.
///

/// details | What if my report is incorrect and uncorroborated?
     {type: question, open: false}
You'll get a refund of your stake without any additional penalties.
///

/// details | What are the consequences of collusion and fraud in reporting?
     {type: question, open: false}
Colluding watchers will lose the amount they staked.
///

/// details | Are permits spent or staked for reporting?
     {type: question, open: false}
Permits are staked, not spent, and can be managed through your dashboard.
///

/// details | Can I adjust my permits?
     {type: question, open: false}
Yes, you can increase or decrease your permits at any time and redeem them when leaving.
///

/// details | How many permits are needed for concurrent reporting?
     {type: question, open: false}
The number depends on bridge activity, with about 160 needed to report one transaction per minute.
///

/// details | Do I still need RSN on Ergo to be a watcher on another chain?
     {type: question, open: false}
Yes, all permit operations are conducted on the Ergo platform, and Rosen's logic is Ergo-based.
///


## Conclusion

With your watcher set up, you are now an integral part of the Rosen ecosystem. Your watcher helps secure cross-chain asset transfers, enabling seamless interoperability between Bitcoin and Ergo.

As the Rosen ecosystem grows, stay tuned for opportunities to earn rewards with your watcher. Thank you for supporting decentralized cross-chain infrastructure!