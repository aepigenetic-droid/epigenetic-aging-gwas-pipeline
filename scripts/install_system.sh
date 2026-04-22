#!/usr/bin/env bash

set -e

echo "Updating system..."
apt-get update

echo "Installing core tools..."
apt-get install -y \
    wget \
    curl \
    unzip \
    gzip \
    bzip2 \
    build-essential \
    python3-dev \
    r-base

echo "System dependencies installed"
