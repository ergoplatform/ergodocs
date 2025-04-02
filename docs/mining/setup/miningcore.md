---
tags:
  - Mining Core
  - miningcore
  - Pool Setup
  - Linux
  - PostgreSQL
  - Guide
---

# 🧱 MiningCore Setup Tutorial for Linux

> 💡 If you're using **Windows 10**, see the [Windows Tutorial](pool_win.md)

---

## Step 1: Download MiningCore

- Clone Mining Core from [GitHub](https://github.com/oliverw/miningcore)

Requirements:

- You must have a working [**PostgreSQL** database](https://www.postgresql.org/download/)
- Ensure you meet all dependencies from the [README](https://github.com/oliverw/miningcore/blob/master/README.md)
- Avoid Docker unless you are confident managing containers

---

## Step 2: Install and Configure PostgreSQL

- For production environments:
      - Monitor I/O, disk, CPU, and memory — MiningCore's API can put heavy load on your DB
      - Keep all PostgreSQL settings default for now
- [Reference setup guide](https://www.postgresqltutorial.com/install-postgresql/)

---

##  Step 3: Create the Database Schema

### Login to PostgreSQL

```bash
sudo -u postgres psql
```

### Create Role and Database

Replace `'your-secure-password'` with a strong password:

```sql
CREATE ROLE miningcore WITH LOGIN ENCRYPTED PASSWORD 'your-secure-password';
CREATE DATABASE miningcore OWNER miningcore;
```

---

## Step 4: Load Schema SQL Files

> ✅ Make sure you can connect using `psql` before proceeding.

- As the `postgres` user, run:

```bash
psql -d miningcore -f miningcore/src/Miningcore/Persistence/Postgres/Scripts/createdb.sql
```

- Then apply the partitioning script:

```bash
psql -d miningcore -f miningcore/src/Miningcore/Persistence/Postgres/Scripts/createdb_postgresql_11_appendix.sql
```

---

##  Step 5: Create a Pool Table

- Run the following command **once per pool** you set up:

```sql
CREATE TABLE shares_mypool1 PARTITION OF shares FOR VALUES IN ('mypool1');
```

- Replace `mypool1` with your pool's unique identifier
- This name is used in the configuration files as well

---

## Step 6: Configure the Pool

- Go to the `build/` directory inside your MiningCore folder
- Create a `<coin>.json` configuration file (e.g. `ergo.json`)
- Refer to: [MiningCore Config Example](https://github.com/oliverw/miningcore/wiki/Configuration) and the example given below. 

/// details | Example Ergo config.json:
     {type: tip, open: false}

### Required Fields in Config

- Replace placeholders:
    - `YOURPOSTGRESQL_PASSWORD_GOES_HERE`
    - `YOUR_REWARD_ADDR_GOES_HERE`
- Adjust:
    - `rewardRecipients` percentage to fit your payout model
    - Enable `paymentProcessing` if you will use automatic share payouts


```
{
    "logging": {
        "level": "info",
        "enableConsoleLog": true,
        "enableConsoleColors": true,
        // Log file name (full log) - can be null in which case log events are written to console (stdout)
        "logFile": "core.log",
        // Log file name for API-requests - can be null in which case log events are written to either main logFile or console (stdout)
        "apiLogFile": "api.log",
        // Folder to store log file(s)
        "logBaseDirectory": "/path/to/logs", // or c:\path\to\logs on Windows
        // If enabled, separate log file will be stored for each pool as <pool id>.log
        // in the above specific folder.
        "perPoolLogFile": false
    },
    "banning": {
        // "integrated" or "iptables" (linux only - not yet implemented)
        "manager": "Integrated",
        "banOnJunkReceive": true,
        "banOnInvalidShares": false
    },
    "notifications": {
        "enabled": true,
        "email": {
            "host": "smtp.example.com",
            "port": 587,
            "user": "user",
            "password": "password",
            "fromAddress": "info@yourpool.org",
            "fromName": "pool support"
        },
        "admin": {
            "enabled": false,
            "emailAddress": "user@example.com",
            "notifyBlockFound": true
        }
    },
    // Where to persist shares and blocks to
    "persistence": {
        // Persist to postgresql database
        "postgres": {
            "host": "127.0.0.1",
            "port": 5432,
            "user": "miningcore",
            "password": "YOURPOSTGRESQL_PASSWORD_GOES_HERE",
            "database": "miningcore"
        }
    },
    // Generate payouts for recorded shares and blocks
    "paymentProcessing": {
        "enabled": true,
        // How often to process payouts, in milliseconds
        "interval": 600,
        // Path to a file used to backup shares under emergency conditions, such as
        // database outage
        "shareRecoveryFile": "recovered-shares.txt"
    },
    // API Settings
    "api": {
        "enabled": true,
        // Binding address (Default: 127.0.0.1)
        "listenAddress": "127.0.0.1",
        // Binding port (Default: 4000)
        "port": 4000,
        // IP address whitelist for requests to Prometheus Metrics (default 127.0.0.1)
        "metricsIpWhitelist": [],
        // Limit rate of requests to API on a per-IP basis
        "rateLimiting": {
            "disabled": false, // disable rate-limiting all-together, be careful
            // override default rate-limit rules, refer to https://github.com/stefanprodan/AspNetCoreRateLimit/wiki/IpRateLimitMiddleware#defining-rate-limit-rules
            "rules": [
                {
                    "Endpoint": "*",
                    "Period": "1s",
                    "Limit": 5
                }
            ],
            // List of IP addresses excempt from rate-limiting (default: none)
            "ipWhitelist": []
        }
    },
    "pools": [
        // Repeat the following section for multiple coins
        {
            // DON'T change the id after a production pool has begun collecting shares!
            "id": "ergo1",
            "enabled": true,
            "coin": "ergo",
            // Address to where block rewards are given (pool wallet)
            "address": "YOUR_REWARD_ADDR_GOES_HERE",
            // Block rewards go to the configured pool wallet address to later be paid out
            // to miners, except for a percentage that can go to, for examples,
            // pool operator(s) as pool fees or or to donations address. Addresses or hashed
            // public keys can be used. Here is an example of rewards going to the main pool
            // "op"
            "rewardRecipients": [
                {
                    // Pool wallet
                    "address": "YOUR_REWARD_ADDR_GOES_HERE",
                    "percentage": 100
                }
            ],
            // How often to poll RPC daemons for new blocks, in milliseconds
            "blockRefreshInterval": 400,
            // Some miner apps will consider the pool dead/offline if it doesn't receive
            // anything new jobs for around a minute, so every time we broadcast jobs,
            // set a timeout to rebroadcast in this many seconds unless we find a new job.
            // Set to zero to disable. (Default: 0)
            "jobRebroadcastTimeout": 10,
            // Remove workers that haven't been in contact for this many seconds.
            // Some attackers will create thousands of workers that use up all available
            // socket connections, usually the workers are zombies and don't submit shares
            // after connecting. This features detects those and disconnects them.
            "clientConnectionTimeout": 600,
            // If a worker is submitting a high threshold of invalid shares, we can
            // temporarily ban their IP to reduce system/network load.
            "banning": {
                "enabled": true,
                // How many seconds to ban worker for
                "time": 600,
                // What percent of invalid shares triggers ban
                "invalidPercent": 50,
                // Check invalid percent when this many shares have been submitted
                "checkThreshold": 50
            },
            // Each pool can have as many ports for your miners to connect to as you wish.
            // Each port can be configured to use its own pool difficulty and variable
            // difficulty settings. 'varDiff' is optional and will only be used for the ports
            // you configure it for.
            "ports": {
                // Binding port for your miners to connect to
                "3052": {
                    // Binding address (Default: 127.0.0.1)
                    "listenAddress": "0.0.0.0",
                    // Pool difficulty
                    "difficulty": 0.02,
                    // TLS/SSL configuration
                    "tls": false,
                    "tlsPfxFile": "/var/lib/certs/mycert.pfx",
                    // Variable difficulty is a feature that will automatically adjust difficulty
                    // for individual miners based on their hash rate in order to lower
                    // networking overhead
                    "varDiff": {
                        // Minimum difficulty
                        "minDiff": 0.01,
                        // Maximum difficulty. Network difficulty will be used if it is lower than
                        // this. Set to null to disable.
                        "maxDiff": null,
                        // Try to get 1 share per this many seconds
                        "targetTime": 15,
                        // Check to see if we should retarget every this many seconds
                        "retargetTime": 90,
                        // Allow time to very this % from target without retargeting
                        "variancePercent": 30,
                        // Do not alter difficulty by more than this during a single retarget in
                        // either direction
                        "maxDelta": 500
                    }
                }
            },
            // Recommended to have at least two daemon instances running in case one drops
            // out-of-sync or offline. For redundancy, all instances will be polled for
            // block/transaction updates and be used for submitting blocks. Creating a backup
            // daemon involves spawning a daemon using the "-datadir=/backup" argument which
            // creates a new daemon instance with it's own RPC config. For more info on this,
            // visit: https:// en.bitcoin.it/wiki/Data_directory and
            // https:// en.bitcoin.it/wiki/Running_bitcoind
            "daemons": [
                {
                    "host": "127.0.0.1",
                    "port": 9052, //ERGO TESTNET DAEMON DEFAULT PORT // MAINNET IS 9053
                    "user": "",
                    "password": "",
                    // Enable streaming Block Notifications via ZeroMQ messaging from Bitcoin
                    // Family daemons. Using this is highly recommended. The value of this option
                    // is a string that should match the value of the -zmqpubhashblock parameter
                    // passed to the coin daemon. If you enable this, you should lower
                    // 'blockRefreshInterval' to 1000 or 0 to disable polling entirely.
                    "zmqBlockNotifySocket": "tcp://127.0.0.1:15101",
                    // Enable streaming Block Notifications via WebSocket messaging from Ethereum
                    // family Parity daemons. Using this is highly recommended. The value of this
                    // option is a string that should  match the value of the --ws-port parameter
                    // passed to the parity coin daemon. When using --ws-port, you should also
                    // specify --ws-interface all and
                    // --jsonrpc-apis "eth,net,web3,personal,parity,parity_pubsub,rpc"
                    // If you enable this, you should lower 'blockRefreshInterval' to 1000 or 0
                    // to disable polling entirely.
                    "portWs": 18545,
                }
            ],
            // Generate payouts for recorded shares
            "paymentProcessing": {
                "enabled": false, //ENABLE FOR SHARE PAYOUT FEATURE
                // Minimum payment in pool-base-currency (ie. Bitcoin, NOT Satoshis)
                "minimumPayment": 0.01,
                "payoutScheme": "PPLNS",
                "payoutSchemeConfig": {
                    "factor": 2.0
                }
            }
        }
        // This section ends here. Add `,` after `}` if this is not the last coin section
    ]
}
```
///


## Step 7: Start the Pool

You should configure your pool to auto-start using a startup script.

```bash
cd build
Miningcore -c <your-config>.json
```

- The JSON config defines the **log files** you should monitor for:
    - Startup errors
    - Daemon issues
    - Pool activity

- You may need to adjust the config to fit your specific pool setup.

---

### ✅ Expected Log Output (Success)

When everything is working properly, your logs should show the following messages:

#### 🟢 Node Online and Synced

```
[2022-03-16 14:26:12.9080] [I] [ergo1] All daemons online
[2022-03-16 14:26:12.9345] [I] [ergo1] Daemon is synced with blockchain
```

#### 🟢 Pool Online

```
[2022-03-16 14:26:14.4346] [I] [ergo1] Pool Online
```

#### 📊 Pool Info Summary

```
Mining Pool:            <YOUR POOL NAME>
Coin Type:              ERG [ERG]
Network Connected:      <testnet|mainnet>
Detected Reward Type:   POW
Current Block Height:   <BLOCKHEIGHT>
Current Connect Peers:  5
Network Difficulty:     <NETWORK DIFF>
Network Hash Rate:      <NETWORK HASHRATE>
Stratum Port(s):        3056, 4056, 3156, 4156
Pool Fee:               <YOUR FEE>
```

> ⚠️ If the **network difficulty** or other values look off, double-check your diff setting in the config.

---

## Step 8: Network Setup Notes

> If your **miner**, **pool**, or **node** are on different machines, you will need to **open ports** to allow communication between them.

### Initial Mining Traffic Flow

- **Miner**  
  → connects to Stratum port (e.g. `3746`)  
- **Pool Server**  
  → connects to Node RPC (mainnet: `9053`, testnet: `9052`)  
- **Node**

Once all components connect, traffic becomes **bi-directional**.

---

### Port Opening Guidelines

- If **all components are on the same machine**:
    - ✅ No need to open ports — uses `localhost`

- If using **LAN or WAN**:
    - 🖥️ Open required ports on your OS firewall
    - 🌐 On WAN, configure **port forwarding** on your router

---

## You're Good to Go!

You now have a fully operational MiningCore pool on Linux.

> Make sure everything is synced, ports are configured, and logs show green — then start mining! ⛏️
