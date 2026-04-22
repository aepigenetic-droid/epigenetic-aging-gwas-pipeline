#!/usr/bin/env bash

set -e

mkdir -p refs/h3k27ac
cd refs/h3k27ac

echo "Downloading H3K27ac peaks..."

# Example fetal enhancer tracks (update if your original file used others)
wget -c https://egg2.wustl.edu/roadmap/data/byFileType/peaks/consolidated/narrowPeak/E091-H3K27ac.narrowPeak.gz
wget -c https://egg2.wustl.edu/roadmap/data/byFileType/peaks/consolidated/narrowPeak/E090-H3K27ac.narrowPeak.gz

echo "H3K27ac download complete"
