# Quick Install

Run the following command to get started

```bash
bash -c "$(curl -s https://node.phenotype.dev)"
```
source available on [GitHub](https://github.com/glasgowm148/ergoscripts)

# Prerequisities 
- Java
- Python
- Windows Subsystem if running Windows

## Java
```bash
curl -s "https://get.sdkman.io" | bash
sdk install java
```

Java 11 is recommended. 

## Python

```bash
# Ubuntu
sudo apt update && upgrade
sudo apt install python3 python3-pip ipython3

# OSX
brew install python
```



## Windows
See [this guide](https://www.windowscentral.com/install-windows-subsystem-linux-windows-10) or run this command in your terminal. This will enable the *Linux Subsystem* and allow you to execute as Linux. 

```bash
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux 
```

## Docker Compose

```yaml
version: "3.8"

services:
  # Ergo blockchain node
  node:
    image: ergoplatform/ergo
    container_name: mn-ergo-node
    command: --mainnet -c /etc/ergo.conf
    volumes:
      - ./.ergo:/home/ergo/.ergo
      - ./ergo.conf:/etc/ergo.conf:ro
    ports:
      - 9053:9053
      - 9030:9030
    restart: unless-stopped
    # Increase or decrease the max heap value as required
    environment:
        - MAX_HEAP=4G
    logging:
      options:
        max-size: "10m"
        max-file: "3"
```

Run the node with

```bash
docker-compose up -d
```

Follow the logs with

```bash
docker logs -f ergo-mainnet -n 200
```