# Bitcoin Rosen Bridge Watcher Setup

To participate as a watcher in the Rosen Bridge, you need to deploy a watcher app that observes one of the supported networks. Each supported network has its own set of watchers responsible for reporting users' actions on that specific network.

## Docker Setup

/// admonition | This section is adapted from the [deploy-docker.md](https://github.com/rosen-bridge/operation/blob/dev/docs/watcher/deploy-docker.md) section on the Rosen Bridge documentation.
    type: info
///




Clone the [Operation repository](https://github.com/rosen-bridge/operation.git) and navigate to the `operation/watcher` directory:

```shell
git clone https://github.com/rosen-bridge/operation.git
cd operation/watcher/
```

Create your environment file `.env` based on the `env.template` file in the `watcher` directory:

```shell
cp env.template .env
```

To view hidden `.env` files later, use `ls -a`.

### Environment Variable Configurations

Configure the required environment variables in the `.env` file (ensure no spaces after the '=' sign):

```shell
# Required Environments

POSTGRES_PASSWORD=your_random_password
POSTGRES_USER=your_random_username
POSTGRES_DB=your_random_db_name
POSTGRES_PORT=5432
```

Set the required permissions and create the `local.yaml` file in the `config` directory:

```shell
sudo chown -R 3000:3000 logs
touch config/local.yaml
```

For MacOS users, set `707` permission for the `logs` directory:

```shell
sudo chmod -R 707 logs
```

//// details | Working with Docker

/// details | Checking logs
{type: info, open: false}
To check logs, use:

```bash
docker compose logs
```

///

/// details | Updating your watcher
{type: info, open: false}
To update your watcher, use:

```bash
docker compose pull
docker compose down
docker compose up -d
```

///

/// details | Restarting your watcher
{type: info, open: false}
To restart your watcher instance, run:

```bash
docker compose up -d
```

///

/// details | no configuration files provided: not found
{type: danger, open: false}
Ensure you're in the correct directory. You should execute `docker compose` commands from within the `operation/watcher` folder.
///

/// details | Dumping databases
{type: info, open: false}
To dump databases, use:

```bash
docker compose down
docker volume remove watcher_postgres-data


#---edit block height in YAML after this step
docker compose up -d
```

///

/// details | Clearing Volumes
{type: info, open: false}
To clear Docker volumes, use:

```bash
docker compose down --volumes
```

Re-initiate the watcher with:

```bash
docker compose up -d
```

///

/// details | Clean Slate
{type: info, open: false}
To remove everything and start from scratch:

```bash
docker ps -a
docker compose down
docker rm CONTAINERID1 CONTAINERID2 CONTAINERID3
```

Then delete the folder and start fresh.
///
////

/// details | Note for Raspberry Pi ARM Users
{type: info, open: false}


To run the watcher on an ARM-based Raspberry Pi, use an ARM-based DB image. Update the `docker-compose.yml` as follows:

Change the DB image according to your architecture (e.g., `arm64v8`):

```diff
services:
  db:
-   image: rapidfort/postgresql:16.0.0
+   image: arm64v8/postgres:16.0
```

Update the volume of the DB:

```diff
    volumes:
-     - postgres-data:/bitnami/postgresql
+     - postgres-data:/var/lib/postgresql/data/
```
///
### Pull Docker Images and Run Service

Pull the Docker image:

```shell
docker compose pull
```

Set up your `local.yaml` using the instructions in the next section (Local Config). After saving the changes, run the container:

```shell
docker compose up -d
```

## Local Config

To start your watcher, configure the `local.yaml` file.

### Specify the Target Network

Set the target network you're watching. Currently supported networks are `ergo`, `cardano`, and `bitcoin`:

```yaml
network: bitcoin
```

### API Configuration

```yaml
api:
  apiKeyHash: "YOUR_API_KEY_HASH"
```

To secure the action-based APIs (e.g., lock, unlock), set a unique and robust API key hash using the Blake2b algorithm. You can generate the hash using the [rosen command line](https://github.com/rosen-bridge/utils/tree/dev/packages/cli):

```shell
npx @rosen-bridge/cli blake2b-hash YOUR_API_KEY
```

Alternatively, use Docker:

```shell
docker run -it --rm node:18.16 npx --yes @rosen-bridge/cli blake2b-hash YOUR_API_KEY
```

### Bitcoin Configuration

Choose your information source for the Bitcoin network and specify its connection information. 

You can use either `rpc`

```yaml
bitcoin:
  type: rpc
  rpc:
    url: "YOUR_RPC_URL"
    username: "YOUR_RPC_USERNAME"
    password: "YOUR_RPC_PASSWORD"
```

//// details | Setting Up a Bitcoin Node (RPC)
{type: info, open: false}
For optimal watcher performance and decentralization, running your own fully synced Bitcoin node is recommended. However, this consumes significant disk space, so you can use a public node as detailed in the next section.

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

/// details | Running a Pruned Bitcoin Node
{type: info, open: false}
A pruned Bitcoin node is not compatible with the Rosen Bitcoin bridge watcher. The watcher requires the `txindex=1` setting, which is not supported by pruned nodes. If you initially synced a pruned node, you'll need to restart the sync with a full node.
///
/// details | Increasing Bitcoin Node DbCache
{type: info, open: false}
To speed up the initial sync of your Bitcoin node, increase the dbcache setting if you have sufficient RAM. For example, to allocate 4GB of cache, add the following line to your bitcoin.conf:

```conf
dbcache=4096
```

Adjust the value based on your available memory.
///
/// details | Current Bitcoin Blockchain Size
{type: info, open: false}
As of June 2024, the Bitcoin blockchain size is approximately 657GB. Keep this in mind when provisioning storage for your Bitcoin node.
///
/// details | Bitcoin Blockchain Snapshots
{type: info, open: false}
Some services provide Bitcoin blockchain snapshots to speed up the initial sync process. However, be cautious when using these snapshots, as they may not be compatible with the txindex=1 requirement for the Rosen Bitcoin watcher. Ensure that the snapshot is from a full node with transaction indexing enabled.
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

Update the `rpc.url` in your watcher's `local.yaml` to point to the remote Bitcoin node's IP address and RPC port:

```yaml
bitcoin:
  type: rpc
  rpc:
    url: "http://<user>:<password>@<remote-ip>:8332"
```

Make sure to configure the Bitcoin node's `rpcallowip` setting to allow connections from the watcher machine's IP.
///
/// details | Enabling Transaction Broadcasting
{type: info, open: false}
If you want your Bitcoin node to be able to broadcast transactions (not required for the watcher but useful for debugging), add the following line to your `bitcoin.conf`:

```conf
zmqpubrawtx=tcp://0.0.0.0:28332
```

This enables the ZeroMQ raw transaction broadcasting feature.
///
////

or `esplora`:

```yaml
bitcoin:
  type: esplora
  esplora:
    url: https://mempool.space
```

Set your watcher's initial height:

```yaml
initial:
  height: LATEST_BITCOIN_HEIGHT
```

Customize observation confirmation and validity threshold:

```yaml
observation:
  confirmation: 2
  validThreshold: 72
```

### Ergo Configuration

/// admonition | **Even if you are running a Bitcoin Watcher, you must configure the Ergo section**
    type: warning
///


Create a new wallet and set the wallet mnemonic:

```yaml
ergo:
  mnemonic: "YOUR_WALLET_MNEMONIC"
```

elect your primary data source:

```yaml
ergo:
  type: node
  node:
    url: https://example.node.com
  explorer:
    url: https://api.ergoplatform.com
```

Set the initial height of your watcher:

```yaml
initialHeight: LATEST_HEIGHT
```

Customize observation confirmation and validity threshold:

```yaml
observation:
  confirmation: 10
  validThreshold: 720
```

### Example Configuration for Bitcoin Watcher

```yaml
network: bitcoin
api:
  apiKeyHash: "YOUR_API_KEY_HASH"
ergo:
  type: explorer
  initialHeight: LATEST_ERGO_HEIGHT
  mnemonic: "YOUR_WALLET_MNEMONIC"
  node:
    url: https://example.node.com
bitcoin:
  type: rpc
  rpc:
    url: "YOUR_BITCOIN_RPC_URL"
    username: "YOUR_RPC_USERNAME"
    password: "YOUR_RPC_PASSWORD"
  initial:
    height: LATEST_BITCOIN_HEIGHT
observation:
  confirmation: 2
  validThreshold: 72
```

## Get Your Watcher Permit

After setting up and running your watcher instance, access the watcher UI by visiting [localhost:3030](http://localhost:3030). From your dashboard, you can view network information, assets, and health status alongside action buttons. To activate your watcher, proceed to the 'LOCK' action, where you can utilize assets from the watcher wallet for registration and obtain reporting permits. Top up your wallet with the specified amounts of ERG and RSN to receive these permits.

As a watcher, your primary responsibility is to monitor your network and report actions related to the bridge. To report a bridge event, you must have report permits. Acquiring these permits involves two types of payments:

1. **Collateral:** Provide one-time collateral in the form of ERG and RSN tokens to obtain initial report permits. This collateral serves as a security measure to mitigate Sybil attacks. When you return all your report permits, the collateral is refunded, and your watcher is unregistered.

2. **RSN for Permits:** Lock RSN tokens to receive permit tokens. Use these tokens to create report permits for reporting events. The number of report permits determines how many concurrent reports you can create. In the event of a valid report, the permit is refunded along with your reward. If the report is invalid, the permit is seized as a penalty.


## Tips


/// details | Interacting with a headless server
     {type: info, open: false}
To interact with a headless server, use SSH (Secure Shell) to establish a secure connection. You can also forward ports to access specific services on the server. For example, forward the local port 3030 to port 3030 on the server:

```bash
ssh -L 3030:127.0.0.1:3030 user@watcher

-server
```

In this command:

- `ssh` starts the SSH client program.
- `-L 3030:127.0.0.1:3030` specifies that the local port 3030 should be forwarded to port 3030 on the server.
- `user@watcher-server` specifies the username and the server to connect to.
  ///


/// details | Security Considerations
{type: warning, open: false}

- Keep your watcher machine and Docker installation updated with the latest security patches.
- Do not reuse your watcher's RPC password anywhere else.
- Secure your machine's SSH login with a strong password and/or public key authentication.
- Consider running the watcher in a dedicated VM or container for isolation.
- Regularly monitor your watcher's logs and web UI for any signs of issues.
- Keep your collateral wallet secure, as the wallet owner has control over unstaking collateral.
  ///

/// details | Monitoring and Alerting
{type: info, open: false}
Maintaining high watcher uptime is critical to avoid collateral penalties. Consider setting up external monitoring and alerting:

- Use services like Uptime Robot or Pingdom to monitor your watcher's web UI and alert you if it goes down.
- Use a service like Healthchecks.io to monitor your watcher's log for error keywords and send alerts.
- The Rosen team's monitoring will alert in Telegram/Discord if your watcher is down, but additional self-monitoring is strongly recommended.
  ///

/// details | Using a Config File for Environment Variables
{type: info, open: false}
Instead of specifying environment variables in the `docker-compose.yml` file, you can use a separate `.env` file. This keeps your compose file cleaner and allows for easier management of environment variables.

Create a `.env` file in the same directory as your `docker-compose.yml` with the following content:

```shell
CURRENT_NETWORK=BITCOIN
DATABASE_URL=file:/app/services/watcher/data/database/data.sqlite
HTTP_PORT=3030
LOGGER_LEVEL=info
```

Update your `docker-compose.yml` to reference these variables:

```yaml
services:
  service:
    image: rapidfort/postgresql:16.0.0
    container_name: watcher_btc
    env_file:
      - .env
    # ... rest of the service definition
```

Docker Compose will automatically load the variables from the `.env` file.
///

## Troubleshooting

UI Errors

/// details | scanner is out of sync
{type: danger, open: false}
Your scanner is out of sync. You need to wait until it scans all blocks. The service runs every 3 minutes. Depending on when it calls and blocks produced, it may drop a block sync here and there but catches up in most cases.

Alternatively, delete Docker volumes and restart your watcher with a newer initial height. Then it doesn't need to scan as many blocks to be synced:

```bash
docker compose down --volumes
```

Then update the `local.yaml` initial height and rerun the watcher.
///

/// details | Permit Health Broken
{type: danger, open: false}
By default, the permit health warning parameter is set to 100. Adjust this locally by adding the following to your `local.yaml`:

```yaml
healthCheck:
  permit:
    warnCommitmentCount: 1 # amount of permits left before giving a warning
    criticalCommitmentCount: 0 # amount of permits left it is critical
```

Adjust the numbers as necessary. `warnCommitmentCount` will change the warning to yellow when the available permits reduce to this number. `criticalCommitmentCount` will change to red when the available permits reduce to this number.
///

/// details | watcher-db-1 is unhealthy
{type: danger, open: false}
If you see "container watcher-db-1 is unhealthy":

- Ensure your `.env` file is correctly named and not `.env.txt`.
- Update your `local.yaml` with the current Ergo block height.

As a last resort, prune existing images and rebuild:

```bash
docker system prune -a
```

**Ensure you don't have other Docker images to worry about.**
///

/// details | Lock, Unlock 500 Error
{type: danger, open: false}
If you receive a 500 error while trying to lock or unlock your ERG and/or RSN, it may be due to an insufficient box value on-chain. **This is fixed in the latest release. Please update if you have not done so already.**

Update with:

```bash
docker compose pull
docker compose down
docker compose up -d
```

Check your service logs first. If you see a warning indicating "Box value BoxValue(1100000) is too low, minimum value for box size of ...", add the following to your `local.yaml` in the `ergo` section:

```yaml
minBoxValue: "2000000"
```

///

/// details | UnhandledPromiseRejection
{type: danger, open: false}
If you encounter an UnhandledPromiseRejection error:

> UnhandledPromiseRejection, promise rejected with reason Object.....LifeCycle script start failed

This is due to an issue in Ogmios roll backward after a fork. A fix is in progress.
///

/// details | The requested image's platform (linux/amd64) does not match the detected host platform
{type: danger, open: false}
This error indicates incompatibility with certain ARM chips in Raspberry Pis and ARM Mac Mini M1 Asahi Linux. See [this PR](https://github.com/rosen-bridge/operation/issues/6).
///

### Operational


/// details | Role and Rewards
{type: question, open: false}
Watchers are essential for accurate reporting and receive 70% of transaction fees as rewards for successful and accurate reporting (while 30% goes to the guard set). 25% of the emission is also reserved for _'Event-Based Emission (Rewards)'_.
///


/// details | Who can become a Watcher?
{type: question, open: false}
Anyone. You can actively contribute to the expansion and security audit of the Rosen Bridge by becoming a watcher. Watchers receive rewards for accurate reporting.

- Configure and run the watcher app for Bitcoin.
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
You don't need to manually watch and approve transactions. The software handles everything automatically. Just ensure the watcher keeps running.

1. Observe an event and wait.
2. Create a commitment using report permits.
3. Aggregate all participating watchers' commitments (into something called event trigger).
4. Wait for guards to take action, especially target chain transactions and reward transactions.
5. Get rewards.
   ///

### Watcher FAQs


/// details | Collateral Requirements
{type: question, open: false}
Each instance requires 800 ERG and 33,000.001 RSN as collateral. This collateral is fully redeemable and the amount is adjustable.
///

/// details | How do I redeem my collateral?
{type: question, open: false}
You can redeem it after redeeming your last permit token. If you have unsettled reports, you must wait until those permits are returned.
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