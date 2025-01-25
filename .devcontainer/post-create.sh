#!/bin/bash

sudo apt-get -y update && sudo apt-get -y upgrade;

# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -;

# Install Poetry dependencies
make install-core;

# Install Node.js and npm
sudo apt install -y nodejs && sudo apt install -y npm;

# Install Node.js dependencies
make install-app;

# Install Docker
sudo apt install -y curl apt-transport-https ca-certificates software-properties-common;
sudo apt install docker.io -y;
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg;
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null;
sudo apt update -y;
sudo apt install docker-ce -y;
sudo usermod -aG docker $USER && newgrp;

# Install Docker Compose
sudo apt-get install -y docker-compose-plugin;
