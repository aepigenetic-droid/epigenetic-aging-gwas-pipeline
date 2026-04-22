#!/usr/bin/env bash

set -e

mkdir -p refs/chromhmm
cd refs/chromhmm

echo "Downloading ChromHMM fetal datasets..."

# Example datasets (replace with exact ones from your original code if needed)
wget -c http://egg2.wustl.edu/roadmap/data/byFileType/chromhmmSegmentations/ChmmModels/coreMarks/jointModel/final/E091_15_coreMarks_dense.bed.gz
wget -c http://egg2.wustl.edu/roadmap/data/byFileType/chromhmmSegmentations/ChmmModels/coreMarks/jointModel/final/E090_15_coreMarks_dense.bed.gz
wget -c http://egg2.wustl.edu/roadmap/data/byFileType/chromhmmSegmentations/ChmmModels/coreMarks/jointModel/final/E084_15_coreMarks_dense.bed.gz

echo "ChromHMM download complete"
