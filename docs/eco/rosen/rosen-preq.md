# Rosen Watcher Prerequisites

## Recommended Hardware Requirements

- **CPU**: 2 cores
- **RAM**: 2 GB
- **Storage**: 20 GB

## Ergo Node

If you aren't running an explorer, you will need to run a node with `ExtraIndex` enabled. This setting, if set to true, allows the node to store all transactions, boxes, and addresses in an index. `extraCacheSize` sets the number of recently used extra indexes kept in memory.

```conf
extraIndex = false
extraCacheSize = 500
```

With your complete config looking something like this

```conf
ergo {
        node {
            mining = false
            extraIndex = true
            extraCacheSize = 500
        }

    }
        
    scorex {
        restApi {
            # Note: you must set a unique password for your API!
            apiKeyHash = "324dcf027dd4a30a932c441f365a25e86b173defa4b8e58948253471b81b72cf"
        }
    }
```

## Docker Compose

Docker Compose is a tool used for defining and running multi-container Docker applications. It uses YAML files to configure the application's services and performs the creation and start-up process of all the containers with a single command. Docker Compose is particularly useful for development, testing, and staging environments, as well as CI workflows.

The recommended method for installing Docker Compose is to install Docker Desktop, which includes Docker Compose, Docker Engine, and Docker CLI. These are all necessary components for running multi-container Docker applications.

You can download Docker Desktop for your specific Operating System from the following link: [Docker Desktop](https://docs.docker.com/desktop/)


