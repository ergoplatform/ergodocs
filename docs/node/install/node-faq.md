# Ergo Node FAQ & Guidelines

## General

### What benefits are there for running a node?

There is no direct financial incentive to run a node. However, doing so contributes to increasing the security of the network.

### Can nodes be viewed anywhere?

Yes, public nodes can be viewed at [ergonodes](http://ergonodes.net/). However, unless your node is hosted on a publicly accessible web-server, your node should be protected by your router.

- To run a public node, refer to this [nginx.conf](https://github.com/glasgowm148/ergoscripts/blob/main/misc/nginx.config) example.
- Be cautious when using a [remote node](https://github.com/ergoplatform/ergo/blob/master/src/main/resources/mainnet.conf) as it can be insecure.



## Minimum Requirements

### Java 

An Ergo node requires a **JDK/JRE version >= 9** installed on your system. We recommend using [Oracle Java SE](https://www.oracle.com/technetwork/java/javase/overview/index.html) or SDKMAN for Unix-based systems:

```bash
curl -s "https://get.sdkman.io" | bash
sdk install java 11.0.13.8.1-amzn
```

### Hardware

The only hardware requirements are ~20GB of storage for the blockchain and ~8GB of RAM for handling the sync. The node utilizes Java, so it should work across all operating systems. You can even run it on a [Raspberry Pi](pi.md). 

> Note: Due to the intensive disk I/O, we recommend having 4-6GB of RAM with a fast SSD, running with the `-Xmx4G` flag on JVM9/11.

## Running the Node



### API Commands

### /node/shutdown

Use the following command to safely shut down your node

```
curl -X POST "http://127.0.0.1:9053/node/shutdown" -H "api_key: hello"
```

If a safe shutdown is not possible, you can terminate the ports:

```
kill -9 $(lsof -t -i:9053)
kill -9 $(lsof -t -i:9030)
```


Please refer to the section on [swagger](../swagger.md) for more information.

### Security

Your node should be protected by your router unless it's running on a publicly accessible web-server. If you wish to host a public node, consider the following:

- The `ergo.conf` file must never be made public.
- Sensitive API methods require a security token that should not be transmitted over untrusted channels.
- Restrict access to the Ergo REST API to known hosts only. Specifically, the API should not be accessible from the Internet.

### Compiling from Source

Instead of downloading the precompiled Ergo jar, you can clone the repository and compile the jar from source using the [`sbt assembly`](https://www.scala-sbt.org/) command.

### Running as a Service

Create a service file:

```
vi /etc/systemd/system/node.service
```

And enter the following content:

```
[Unit]
Description=ErgoNode Service
[Service]
User=user
WorkingDirectory=/mnt/HC_Volume_19304500/ergo
ExecStart=/mnt/HC_Volume_19304500/run_node.sh
SuccessExitStatus=143
TimeoutStopSec=10
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Next, create the `sh` file:

```bash
echo "#!/bin/sh
sudo /usr/bin/java -jar -Xmx4G ergo.jar --mainnet -c ergo.conf" > run_node.sh
chmod +x run_node.sh
```

Finally, enable and start the service:

```
sudo systemctl daemon-reload
sudo systemctl enable node.service
sudo systemctl start node
sudo systemctl status node
```
