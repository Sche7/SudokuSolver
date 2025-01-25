#!/bin/bash

sudo apt-get -y update && sudo apt-get -y upgrade;

# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -;

# Install Poetry dependencies
make install-core;

# Install Node.js and npm
sudo apt install nodejs -y && sudo apt install npm -y;

# Install Node.js dependencies
make install-app;
