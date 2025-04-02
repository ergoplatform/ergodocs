---
tags:
  - Rosen Bridge
  - Watcher
  - Setup
  - Guide
  - FAQ
  - Troubleshooting
  - Cross-chain
  - Oracle
---

# Ergo Rosen Bridge Watcher Setup

Watchers are integral to Rosen Bridge, serving as cross-chain oracles. They observe and report deposit events on their network to Ergo, contributing to the network's security and expansion.

## Watcher Setup Guides



//// details | Tutorials
     {type: info, open: true}
/// details | Pre-requisites
     {type: danger, open: true}
See the [pre-requisites page](rosen-preq.md) for information on setting up a local node, as well as minimal hardware and software requirements. (Docker)
///
There is a [General Watchers app Tutorials Playlist](https://youtube.com/playlist?list=PLyQeADPK2PWgztdc9lCvAyqjknPaN9woQ&si=SNYxoZMv2iID610o), and more tailored guides for each platform available:

/// details | Windows
     {type: info, open: false}
- Follow along as QX guides you through a [Windows Watcher installation](https://www.youtube.com/watch?time_continue=2&v=bQ2sviHtOQA&embeds_referring_euri=https%3A%2F%2Fwww.therefour.org%2F&embeds_referring_origin=https%3A%2F%2Fwww.therefour.org&source_ve_path=Mjg2NjY&feature=emb_logo)
- [Rosen Bridge Watcher — Windows Setup Guide](https://medium.com/@goatspark/rosen-bridge-watcher-windows-setup-guide-4040815e0a74)
///
/// details | Mac
     {type: info, open: false}
- [Rosen Watcher with Mac (ErgoTutorials)](https://ergotutorials.com/video/rosen-bridge)
///
/// details | Linux
     {type: info, open: false}
mgpai walks through a Watcher instance in [Linux and Cloud](https://www.youtube.com/watch?time_continue=1&v=1dpfLWdWMLs&embeds_referring_euri=https%3A%2F%2Fwww.therefour.org%2F&embeds_referring_origin=https%3A%2F%2Fwww.therefour.org&source_ve_path=MjM4NTE&feature=emb_title)
///

    


Below you'll find some frequently asked questions as well as common issues and troubleshooting tips.
////





## Watcher FAQs

### Operational

/// details | Role and Rewards
     {type: question, open: false}
Watchers are essential for accurate reporting and receive 70% of transaction fees as rewards for successful and accurate reporting. (while 30% goes to the guard set). 25% of the emission is also reserved for *'Event-Based Emission (Rewards)'*
///

/// details | Who can become a Watcher?
     {type: question, open: false}
Anyone. You can actively contribute to the expansion and security audit of the Rosen Bridge by becoming a Watcher. Watchers receive rewards for accurate reporting.

- Configure and run the Watcher app for your desired network (In progress, so stay tuned!).
- Top it off with enough RSN and ERG.
- Put in collateral and receive reporting permits.
- Enjoy reporting and getting rewards.
///

/// details | Is there a limit on the number of watchers?
     {type: question, open: false}
77 is the one repo's capacity and cannot be changed, but we'll open other repos. So technically, we can have any number of repos that each has 77 watchers. However, in long run I assume one or two repos is sufficient for each network.

A minimum of 60%+1 of the total number of watchers is required to trigger an event, adjustable by the guard set.
///

/// details | Can I run multiple watchers?
     {type: question, open: false}
Yes, but it incurs financial considerations to prevent abuse. Each instance needs a unique folder and WATCHER_PORT.
///

### Collateral, Permits and Reporting

/// details | Collateral Requirements
     {type: question, open: false}
Each instance requires 800 ERG and 30,000 RSN as collateral. This collateral is fully redeemable and the amount is adjustable.
///

/// details | How do I redeem my collateral?
     {type: question, open: false}
You can redeem it after redeeming your last permit token, but if you have unsettled reports, you must wait until those permits are returned.
///

/// details | Permit Acquisition
     {type: question, open: false}
To report, watchers must acquire permits, costing an additional 3,000 RSN. Multiple permits are necessary for reporting concurrent events, and permits can be seized if reports are found fraudulent.
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


## Operational

/// details | Do I need to do anything after setup?
     {type: question, open: false}
You don't need to manually watch and approve transactions, the software will handle everything automatically, you just need to ensure the watcher keeps running.

1. Observe an event and wait a bit.
2. Create a commitment using report permits.
3. Aggregate all participating watchers commitment (into something called event trigger).
4. Wait for guards stuff, especially target chain tx and reward tx submission.
5. Get rewards.
///




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

### UI Errors

/// details | scanner is out of sync
     {type: danger, open: false}

Your scanner is out of sync. You need to wait until it scan all blocks. The service runs every 3 minutes or so. Depending on when it calls and blocks produced it may drop a block sync here and there but catches up in most cases.

Alternatively you can delete docker volumes and restart your watcher with newer initial height

Then it doesn't need to scan that much blocks to be synced

```bash
docker compose down --volumes
```

Then update the `local.yaml` initial height

Then rerun the watcher
///

/// details | Permit Health Broken
     {type: danger, open: false}

By default, the permit health warning parameter is set to 100. This is adjustable locally by adding the following into your local.yaml and adjusting as neccessary


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

- Your .env file might be missing? turn on view file extensions like in the video, are you sure it's .env and not .env.txt?
- update your local.yaml with the current ergo blockheight

As a last resort, some ssers are reporting that this issue can be fixed by pruning existing images and rebuilding 

```
docker system prune -a
``` 

**As long as you don't have other docker images to worry about.**

///






/// details | Lock, Unlock 500 Error
     {type: danger, open: false}

If you're receiving a 500 Error while trying to lock or unlock your ERG and/or RSN, it could possibly be from having an insufficient box value on chain. **This is fixed in the latest release, please update if you have not done so already.**

Update with 
```
docker-compose pull
docker-compose down
docker-compose up -d
```

please check your service logs first. If you see a warning indicating "Box value BoxValue(1100000) is too low, minimum value for box size of ..."

To rectify, add the following to your local.yaml in the "ergo:" section with one tab indent. (should be the same indent as `initialHeight`).

```yaml
  minBoxValue: '2000000'
```
///

/// details | UnhandeledPromiseRejection
     {type: danger, open: false}
> UnhandeledPromiseRejection, promise rejected with reason Object.....LifeCycle script start failed

There is a issue in ogmios roll backward after a fork. Fix is a work in progress.
///

/// details | The requested image's platform (linux/amd64) does not match the detected host platform
     {type: danger, open: false}
Incompatiblility with certain ARM chips in Rasberry Pi's and (ARM mac mini m1 Asahi linux: see [this PR](https://github.com/rosen-bridge/operation/issues/6))
///



### Working with docker

/// details | Checking logs
     {type: info, open: false}
```bash
docker compose logs
```

///


/// details | Updating your watcher
     {type: info, open: false}
```bash
docker-compose pull
docker-compose down
docker-compose up -d
```
///

/// details | Restarting your watcher
     {type: info, open: false}
You can restart your watcher instance simply by running the following command from within the same folder the `docker-compose.yaml` is stored.

```bash
docker compose up -d
```

///

/// details | no configuration files provided: not found
     {type: danger, open: false}

Check you're in the correct directory. You should be executing `docker compose` commands from within the `operation/watcher` folder
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
You may wish to clear Docker volumes for a number of reasons, e.g. changing Initial_Height to sync. To do so run the following Docker command from the Watcher directory

```bash
docker compose down --volumes
```
Re-initiate the Watcher with
```bash
docker compose up -d
```
///

/// details | Clean Slate
     {type: info, open: false}
If you want to remove everything and start from scratch

```bash
docker ps -a
docker compose down
docker rm CONTAINERID1 CONTAINERID2 CONTAINERID3
```
then delete the folder and start fresh
///
