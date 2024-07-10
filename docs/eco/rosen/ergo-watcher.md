# Ergo Rosen Bridge Watcher Setup

Watchers are integral to Rosen Bridge, serving as cross-chain oracles. They observe and report deposit events on their network to Ergo, contributing to the network's security and expansion.

/// admonition | This section is adapted from the [deploy-docker.md](https://github.com/rosen-bridge/operation/blob/dev/docs/watcher/deploy-docker.md) section on the Rosen Bridge documentation.
    type: info
///


## Clone the Repository and Prepare the Environment
First, clone the operational repository and navigate to the appropriate directory:

```shell
git clone https://github.com/rosen-bridge/operation.git
cd operation/watcher/
```

Create and configure the environment file from the template provided:

```shell
cp env.template .env
# Edit the .env file to set POSTGRES_PASSWORD, POSTGRES_USER, POSTGRES_DB, and POSTGRES_PORT
```

## Configure Environment Variables and Permissions
Set up necessary environment variables in the `.env` file and adjust file permissions:

```shell
# Example environment variables setting
POSTGRES_PASSWORD=your_password # a random alphanumeric password without special characters (like $%!-#)
POSTGRES_USER=your_user # a random name
POSTGRES_DB=your_db # a random name
POSTGRES_PORT=5432 # 5432 is set as default, you can change it
# Set permissions and create local.yaml
sudo chown -R 3000:3000 logs
touch config/local.yaml
```

For MacOS users, adjust the permissions for the `logs` directory:

```shell
sudo chmod -R 707 logs
```

## Configure Docker for ARM Devices (if applicable)

/// details | Raspberry Pi ARM 
     {type: info, open: false}

If you're running on a Raspberry Pi ARM device, specify an ARM-compatible Docker image and adjust the volume mapping in the docker-compose file:

```yaml
# Example docker-compose configuration for ARM64v8
db:
  image: arm64v8/postgres:16.0
  env_file:
    - .env
  volumes:
    - postgres-data:/var/lib/postgresql/data/
  networks:
    - rosen_network
  restart: always
  healthcheck:
    test: ['CMD-SHELL', 'pg_isready -U $$POSTGRES_USER -d $$POSTGRES_DB']
    interval: 10s
    timeout: 5s
    retries: 3
```
///

## Pull Docker Images and Start the Watcher
Before starting the watcher, pull the necessary Docker images and run the service:

```shell
docker compose pull
docker compose up -d
```


### Configure the `local.yaml` File for Ergo
Set up the `local.yaml` configuration file specifically for the Ergo network:

```yaml
network: ergo
api:
  apiKeyHash: 'YOUR_API_KEY_HASH'
ergo:
  type: node
  initialHeight: <latest height>
  mnemonic: 'YOUR_WALLET_MNEMONIC'
  node:
    url: 127.0.0.1:9053
observation:
  confirmation: 10
  validThreshold: 720
```

Make sure to use the actual values and URLs as per your setup requirements.

## Start the Watcher and Monitor
After configuring all files and setting up the environment, start the watcher:

```shell
docker compose up -d
```

Access the watcher UI by visiting `http://localhost:3030` to monitor network information and health status.

## Note
- Adjust the `apiKeyHash` and `mnemonic` in the `local.yaml` or through the `.env` file for added security.
- Ensure your Docker environment is properly configured, especially when deploying on different architectures like ARM.
- Regularly update your configuration files and Docker images to keep up with network changes and software updates.


/// admonition | For tips, troubleshooting, FAQs, and other information, please refer to the main [watcher documentation](watcher.md).
    type: info
///
