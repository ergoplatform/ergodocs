#!/bin/bash


## Rosen Bridge Watcher with Ergo configuration

## Steps to use
### Download this file as rosen_install.sh
### chmod +x rosen_install.sh
### ./rosen_install.sh

# Exit immediately if a command exits with a non-zero status.
set -e
# Function to install Docker and Docker Compose
install_docker() {
    echo "Installing Docker..."
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        sudo apt-get update
        sudo apt-get install -y docker-ce docker-ce-cli containerd.io

        echo "Installing Docker Compose..."
        sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
        sudo chmod +x /usr/local/bin/docker-compose
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        # Assumes Homebrew is installed on macOS
        brew cask install docker

        # Docker for Mac includes Compose, no separate installation required
    fi
    echo "Docker and Docker Compose installed successfully."
}

# Function to install PostgreSQL
install_postgres() {
    echo "Installing PostgreSQL..."
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        sudo apt-get update
        sudo apt-get install -y postgresql postgresql-contrib
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        # Assumes Homebrew is installed on macOS
        brew install postgresql
    fi
    echo "PostgreSQL installed successfully."
}

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    install_docker
else
    echo "Docker is already installed."
fi

# Check if PostgreSQL is installed
if ! command -v psql &> /dev/null; then
    install_postgres
else
    echo "PostgreSQL is already installed."
fi

# Prompt for environment variables
read -p "Enter your POSTGRES_PASSWORD: " POSTGRES_PASSWORD
read -p "Enter your POSTGRES_USER: " POSTGRES_USER
read -p "Enter your POSTGRES_DB: " POSTGRES_DB
POSTGRES_PORT=5432 # Default port, change if needed
read -p "Enter your MNEMONIC: " MNEMONIC
read -p "Enter your API_PASS: " API_PASS

# Create a new directory for the node and navigate into it
mkdir -p node && cd node

# Set up the `ergo.conf`
echo "
    ergo {
        node {
            mining = false
            extraIndex = true
            extraCacheSize = 500
        }

    }
        
    scorex {
        restApi {
            apiKeyHash = \"324dcf027dd4a30a932c441f365a25e86b173defa4b8e58948253471b81b72cf\"
        }
    }" > ergo.conf

# Populate docker-compose.yml
echo "version: \"3.8\"

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
    environment:
        - MAX_HEAP=4G
    logging:
      options:
        max-size: \"10m\"
        max-file: \"3\"" > docker-compose.yml

# Run the node
docker-compose up -d

# Navigate back to the parent directory
cd ..

# Clone the operation repository
git clone https://github.com/rosen-bridge/operation.git
cd operation/watcher/

# Copy the environment template file
cp env.template .env

# Set the required environment variables
echo "POSTGRES_PASSWORD=$POSTGRES_PASSWORD
POSTGRES_USER=$POSTGRES_USER
POSTGRES_DB=$POSTGRES_DB
POSTGRES_PORT=$POSTGRES_PORT" >> .env

# Set permissions for logs directory
sudo chown -R 3000:3000 logs
if [[ "$OSTYPE" == "darwin"* ]]; then
    sudo chmod -R 707 logs
fi
# Pull Docker images
docker compose pull

# Create local.yaml
touch config/local.yaml

# Fetch PEER_HEIGHT
## Note: Please update this when your sync is done
PEER_HEIGHT=$(curl --silent --max-time 10 -X GET "http://localhost:9053/info" -H "accept: application/json" | python -c "import sys, json; print(json.load(sys.stdin)['maxPeerHeight']);")

# Populate config/local.yaml
echo "network: ergo
ergo:
  type: node
  initialHeight: \$PEER_HEIGHT
  mnemonic: \$MNEMONIC
  node:
    url: http://127.0.0.1:9053/
  transaction:
    commitmentTimeoutConfirmation: 720

observation:
  confirmation: 10
  validThreshold: 720" > config/local.yaml

# Update config/local.yaml with actual values
sed -i '' "s/\$PEER_HEIGHT/$PEER_HEIGHT/; s/\$MNEMONIC/$MNEMONIC/" config/local.yaml

# Set BLAKE_HASH and update ergo.conf
cd ../../node
BLAKE_HASH=$(curl --silent -X POST "http://localhost:9053/utils/hash/blake2b" -H "accept: application/json" -H "Content-Type: application/json" -d "\"$API_PASS\"")
sed -i '' "s/apiKeyHash = .*/apiKeyHash = $BLAKE_HASH/" ergo.conf
docker restart mn-ergo-node

echo "Rosen Watcher setup completed."
