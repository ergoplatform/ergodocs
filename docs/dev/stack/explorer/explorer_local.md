# Explorer

## Intro 

The Ergo Blockchain Explorer is your interface with the blockchain and provides four services. 

1. `modules/chain-grabber`: Dumps aggregated data blockchain -> database
2. `modules/explorer-api`: Provides a set of HTTP API methods for querying on/off-chain data.
3. `modules/utx-tracker`: Dumps unconfirmed transactions from the mempool to local database
4. `modules/utx-broadcaster`: Broadcasts unconfirmed transactions to a set of known peers

## Sources

- [explorer-backend](https://github.com/ergoplatform/explorer-backend)
- [explorer-frontend](https://github.com/ergoplatform/explorer-frontend)


## Resources

- [Deploying Explorer services with Docker Compose](https://github.com/ergoplatform/explorer-backend/wiki/Deploying-explorer-services-with-docker-compose)
- [How to setup the Chain-Grabber module on a Raspberry Pi device](rpi-blockchain-explorer.md)
- [Ergo Nix Toolkit](https://github.com/ergoplatform/ergo-nix)
- [Ergo Bootstrap](https://github.com/ergoplatform/ergo-bootstrap)
- [ergo-setup](https://github.com/abchrisxyz/ergo-setup) is a Docker based Ergo setup (Node, Explorer & GraphQL). Somewhat similar to Ergo Bootstrap except it offers much less options and is not NixOS-based.


## Running your own instance of Explorer 

First we'll create a working directory and `cd` into it. 

```bash
mkdir explorer && cd "$_"
```

### Creating env files


> `.db_env` 

```bash
echo "DB_URL=jdbc:postgresql://postgres:5432/explorer
DB_USER=postgres
DB_PASS=1234" > .db_env
```

> `.redis_env` 

```bash
echo "REDIS_URL=redis://localhost:6379" > .redis_env
```

Additional configurations are made by adding entries to the `env_file` field in `docker-compose.yaml`. ie, `.http_env`



### explorer-frontend

```bash
git clone https://github.com/ergoplatform/explorer-frontend
sudo mkdir -p front/build
sudo cp -r explorer-frontend/build /front
sudo mkdir front/config
sudo vi front/config/app.config.js
sudo vi docker-compose.yaml
```

### explorer-backend

```bash
git clone https://github.com/ergoplatform/explorer-backend
cd explorer-backend/modules

# All vars for the .x_env files are listed
# in default config of the corresponding service
vi chain-grabber/src/main/resources/application.conf
vi explorer-api/src/main/resources/application.conf
vi utx-tracker/src/main/resources/application.conf
vi utx-broadcaster/src/main/resources/application.conf

# Create docker network 
docker network create explorer-network
```

### Booting

> Configure other services (such as: nginx, postgres, redis, adminer) according to their documentaion

```bash
# Run from /explorer/
docker-compose up -d

# To make sure everything up and working.
docker ps -a
```


### Files
> paste the following into `app.config.js`

- `apiUrl` points to your to backend API. 
- `environments.url` points to your frontend

```bash
var __APP_CONFIG__ = {
  apiUrl: 'https://api.ergoplatform.org',
  alternativeLogo: false, // true by default
  environments: [
     {
       name: 'Mainnet',
       url: 'https://explorer.ergoplatform.org',
     },
  ],
};

if (typeof global !== 'undefined') {
  global.__APP_CONFIG__ = __APP_CONFIG__;
}
```

> `docker-compose.yaml`

```yaml
version: '3.4'

services:
  nginx:
    image: nginx:1.17.9-alpine
    ports:
      - "443:443"
    volumes:
      - /data/nginx/nginx.conf:/etc/nginx/nginx.conf:ro
      - /data/nginx/ssl:/etc/ssl:ro
      - /explorer/front/build:/usr/share/nginx/html
      - /explorer/front/config:/usr/share/nginx/config
    networks:
      - explorer-network
    depends_on:
      - api
  postgres:
    image: postgres:11-alpine
    shm_size: 2g
    environment:
      POSTGRES_PASSWORD: <password>
    ports:
      - "5432:5432"
    volumes:
      - /data/postgres:/var/lib/postgresql/data:rw
    networks:
      - explorer-network
  redis:
    image: redis:latest
    restart: always
    command: ["redis-server"]
    ports:
      - "127.0.0.1:6379:6379"
    volumes:
      - /data/redis:/usr/local/etc/redis
    networks:
      - explorer-network
  adminer:
    image: adminer:4-standalone
    ports:
      - "8082:8080"
    networks:
      - explorer-network
  grabber:
    image: oskin1/chain-grabber:latest
    networks:
      - explorer-network
    env_file:
      - .db_env
    depends_on:
      - postgres
  api:
    image: oskin1/explorer-api:latest
    ports:
      - "8081:8081"
    networks:
      - explorer-network
    env_file:
      - .db_env
    depends_on:
      - postgres
      - redis
  utx-tracker:
    image: oskin1/utx-tracker:latest
    networks:
      - explorer-network
    env_file:
      - .db_env
    depends_on:
      - postgres
  utx-broadcaster:
    image: oskin1/utx-broadcaster:latest
    networks:
      - explorer-network
    env_file:
      - .redis_env
    depends_on:
      - redis

networks:
  explorer-network:
    external: true
```


## Manual Instance

### Prerequsites

```
sudo apt update
sudo apt full-upgrade

## SDKMAN
curl -s "https://get.sdkman.io" | bash
sdk install java
sdk install sbt

## PostgreSQL
sudo apt install postgresql
sudo su postgres
createuser ergo -P --interactive
```

Load database schema
```
psql
create database explorer;
\c explorer;
\i /explorer-backend/modules/explorer-core/src/main/resources/db/V9__Schema.sql
```




```
docker build explorer-backend/modules/chain-grabber/
docker build explorer-backend/modules/chain-grabber/
docker build explorer-backend/modules/chain-grabber/
docker build explorer-backend/modules/chain-grabber/
```

