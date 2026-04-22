#!/usr/bin/env bash

set -e

mkdir -p refs/ldsc/weights
cd refs/ldsc/weights

echo "Downloading regression weights..."
wget https://data.broadinstitute.org/alkesgroup/LDSCORE/weights_hm3_no_hla.tgz

tar -xzvf weights_hm3_no_hla.tgz

echo "Weights ready"
