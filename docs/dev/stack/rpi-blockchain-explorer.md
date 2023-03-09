
# Tutorial: Blockchain Explorer with Raspberry Pi

## How to setup the Chain-Grabber module on a Raspberry Pi device

This is a guide for developers and data scientists interested in storing the Ergo blockchain to a standardized database format using a Raspberry Pi.

We will focus specifically on the Chain Grabber module from the [Ergo Blockchain Explorer (backend)](https://github.com/ergoplatform/explorer-backend).

### Prerequisites

* Raspberry Pi with official OS installed
* Minimum 60GB of disk space available
* SSH enabled with stable internet connection

<br>

### Preparing the RPi
```bash
sudo apt update
sudo apt full-upgrade
```

### Download latest Java version
```bash
sudo apt install default-JDK
```

### Download sbt
```bash
echo "deb https://repo.scala-sbt.org/scalasbt/debian /" | sudo tee -a /etc/apt/sources.list.d/sbt.list
curl -sL "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x2EE0EA64E40A89B84B2DF73499E82A75642AC823" | sudo apt-key add
sudo apt update
sudo apt install sbt
```

### Download and unzip precompiled JAR

If you are reading this in the future, please visit the [code release repo](https://github.com/ergoplatform/explorer-backend/releases) and replace it with the appropriate version.

```bash
wget https://github.com/ergoplatform/explorer-backend/archive/refs/tags/<version>.zip

unzip explorer-backend-<version>
```

### Install PostgreSQL

In the code snippet below, we created "ergo" as the username.

```bash
sudo apt install postgresql
sudo su postgres
createuser ergo -P --interactive
```

### Setup and load database schema
```bash
psql
create database explorer;
\c explorer;
\i /explorer-backend-9.4.3/modules/explorer-core/src/main/resources/db/V9__Schema.sql
```
The final line of code above executes a SQL script that creates a bunch of tables and indices to be populated later by the Chain Grabber.



### Update app config

This is where you need to edit the database username and password you set up earlier. 

```bash
sudo nano explorer-backend-9.4.3/modules/chain-grabber/src/main/resources/application.conf
```

### Launch chain-grabber

Run the following command from within the `explorer-backend` directory. 
```bash
sbt chain-grabber/run
```

### Validate

If all goes well, the code below returns the latest block height that was stored in the database.

```bash
select max(height) from node_headers;
```



