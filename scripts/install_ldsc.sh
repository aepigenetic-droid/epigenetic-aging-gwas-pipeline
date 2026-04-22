#!/usr/bin/env bash

set -e

mkdir -p refs/ldsc

if [ ! -f "refs/ldsc/ldsc.py" ]; then
    echo "Cloning LDSC repository..."
    git clone https://github.com/bulik/ldsc.git refs/ldsc
else
    echo "LDSC already exists, skipping clone."
fi

echo "LDSC setup complete."
