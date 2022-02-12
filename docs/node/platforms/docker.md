# Docker

## Docker


## Docker Compose

```
version: "2"

services:
  node:
    image: ergoplatform/ergo
    container_name: ergo-mainnet
    ports:
      - 9053:9053
      - 9030:9030
    environment:
      - MAX_HEAP=3G
    volumes:
      - ~/.data/ergo/mainnet:/home/ergo/.ergo
      - ./myergo.conf:/etc/myergo.conf
    restart: unless-stopped
    command: --mainnet -c /etc/myergo.conf
```

Run the node with

```
docker-compose up -d
```

Follow the logs with
```
docker logs -f ergo-mainnet -n 200
```