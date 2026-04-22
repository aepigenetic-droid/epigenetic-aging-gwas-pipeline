#!/usr/bin/env bash

set -e

mkdir -p refs/ldsc
cd refs/ldsc

echo "Downloading LD scores..."
wget https://data.broadinstitute.org/alkesgroup/LDSCORE/eur_w_ld_chr.tar.bz2

tar -xvjf eur_w_ld_chr.tar.bz2

echo "LD scores ready"
