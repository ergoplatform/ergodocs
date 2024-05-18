# Miningcore

The following tutorial is written for Linux; see [this page if you're using Windows 10](pool_win.md)

### Download [miningcore](https://github.com/oliverw/miningcore)  

- You must deploy a working [**PostgreSQL** database](https://www.postgresql.org/download/)

### Install and configure PostgreSQL

If you are deploying in production, you need to be careful on I/O and disk/CPU/memory as a public Miningcore API will pound on your database. Keep all things default for now; here's a [good simple article](https://www.postgresqltutorial.com/install-postgresql/)

Installing Miningcore will depend if you are on Windows or Linux. Pay close attention to the dependencies needed as depicted in the [README](https://github.com/oliverw/miningcore/blob/master/README.md). Stay away from docker unless you're sure. 

### Load the schema  

Miningcore operates under the schema `miningcore` by default.  

**Login to Postgres** 

```bash
sudo -u postgres psql
```

**Create schema**

```SQL
CREATE ROLE miningcore WITH LOGIN ENCRYPTED PASSWORD 'your-secure-password';
CREATE DATABASE miningcore OWNER miningcore;
```

**Load the schema.** 

> You MUST be able to connect to your database with the `psql` command before trying this.  

As the Postgres operating system user, run:

```SQL
psql -d miningcore -f miningcore/src/Miningcore/Persistence/Postgres/Scripts/createdb.sql
```

**Apply partitions for the shares table. **

Do this upfront even if you don't think you will need it:

```SQL
psql -d miningcore -f miningcore/src/Miningcore/Persistence/Postgres/Scripts/createdb_postgresql_11_appendix.sql
```

**Create your new pool. **

You do this ONCE for each new pool you create. 

```SQL
CREATE TABLE shares_mypool1 PARTITION OF shares FOR VALUES IN ('mypool1');
```

`mypool1` becomes the unique identifier for your pool. Name it wisely 

Configure a pool config named <something>.json, and place it in the build directory of miningcore. 

Miningcore config.json example: https://github.com/oliverw/miningcore/wiki/Configuration

Example Ergo config.json:

(NOTE: You MUST update the YOURPOSTGRESQL_PASSWORD_GOES_HERE and YOUR_REWARD_ADDR_GOES_HERE variables if copy and pasting this config as well modify the rewardRecipients percentage to fit your pool's scheme and enable the paymentProcessing section if you plan to utilize share payouts for your pool)
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




### Start the pool 

You should configure it to auto-start via a startup script. 

```
cd build
Miningcore -c <your config>.json
```

We use a different pool-specific startup configuration, so you may have to play around with it. The JSON config specifies the log files you should look at for startup errors/issues/etc. If you got this far, below is the startup log message you should get indicating you are running a healthy miningcore ergo pool:

**Indicates your Node is online and synced**

```
[2022-03-16 14:26:12.9080] [I] [ergo1] All daemons online
[2022-03-16 14:26:12.9345] [I] [ergo1] Daemon is synced with blockchain
```

**Indicates Pool is online**
```
[2022-03-16 14:26:14.4346] [I] [ergo1] Pool Online
```
Indicates the diff setting, your fee, and that its a go:
```
Mining Pool:            <YOUR POOL NAME>
Coin Type:              ERG [ERG]
Network Connected:      <testnet|mainnet>
Detected Reward Type:   POW
Current Block Height:   <BLOCKHEIGHT>
Current Connect Peers:  5
Network Difficulty:     <NETWORK DIFF>
Network Hash Rate:      <NETWORK HASHRATE>
Stratum Port(s):        3056, 4056, 3156, 4156  <THIS SHOULD BE THE PORTS YOU HAVE CONFIGURED>
Pool Fee:               <YOUR FEE>
```

Pay close attention to the stats above in regards to the network. If your diff setting is wrong, the network difficulty won't be right.

> If you host your miner, pool, or node on separate machines, you'll need to open ports to allow that traffic.

**Illustration of initial mining traffic:**

- Miner -> 
    - (connects on your defined Stratum port i.e. `3746`) -> 
- pool server -> 
    - connects to node RPC (`9053`, mainnet or `9052`, testnet) -> 
- node
  
Once connections are established, traffic becomes bi-directional.

**You will not need to open ports if any of the above layers are on the same machine.**  Internal traffic runs via the internal loop (localhost). 

Typically, machines block incoming traffic (but allow outgoing) by default. If you're testing on LAN, you'll need to open these ports on your OS's firewall. But when you get to WAN, you'll additionally need to set up port forwarding on your network router.
