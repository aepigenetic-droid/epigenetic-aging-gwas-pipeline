# Epigenetic Aging GWAS Pipeline

## End-to-end GWAS, LDSC, and Epigenomic Annotation Framework for Biological Aging Analysis

---

## Overview

This repository provides a fully reproducible computational pipeline for analyzing genome-wide association study (GWAS) summary statistics in the context of biological aging. The framework integrates GWAS processing, linkage disequilibrium score regression (LDSC), and epigenomic annotation layers (ChromHMM and H3K27ac) to connect genetic variation with regulatory mechanisms relevant to aging.

The pipeline is designed to be modular, extensible, and executable across environments without reliance on notebook-based workflows.

---

## Key Features

* Automated GWAS ingestion and harmonization
* Quality control and allele standardization
* LDSC-based heritability and genetic correlation analysis
* Integration of epigenomic annotations (ChromHMM, H3K27ac)
* Consensus enhancer construction
* Fully script-based execution (no notebook dependencies)
* Reproducible and publication-ready outputs

---

## Pipeline Structure

The workflow is organized into four sequential phases:

### Phase A: Setup and Reference Data

* Directory structure creation
* Environment and dependency checks
* Download of LD reference data (HapMap3, LD scores, baselineLD, weights)

### Phase B: GWAS Processing

* Trait metadata definition
* GWAS download or ingestion
* VCF to summary statistics conversion
* Harmonization and QC
* Allele standardization and SNP filtering

### Phase C: LDSC Analysis

* Munge summary statistics
* SNP heritability estimation (h²)
* Genetic correlation (rg)
* Parsing and extraction of LDSC outputs

### Phase D: Epigenomic Annotation

* ChromHMM segmentation download
* H3K27ac enhancer data integration
* Consensus enhancer construction
* Annotation quality control

---

## Repository Structure

```
epigenetic-aging-gwas-pipeline/

├── config/
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
│
├── refs/
│   ├── ldsc/
│   ├── baselineLD/
│   └── hm3/
│
├── outputs/
│   ├── ldsc/
│   ├── logs/
│   └── figures/
│
├── src/
│   ├── setup/
│   ├── reference/
│   ├── gwas/
│   ├── ldsc/
│   ├── annotations/
│   └── utils/
│
├── scripts/
├── run_pipeline.py
├── requirements.txt
├── environment.yml
└── README.md
```

---

## Installation

### Option 1: Conda (recommended)

```
conda env create -f environment.yml
conda activate epigenetic-aging
```

### Option 2: pip

```
pip install -r requirements.txt
```

---

## System Requirements

* Python 3.9+
* R (for LDSC compatibility)
* Linux or Unix-based environment recommended
* Internet access for downloading reference datasets

---

## Running the Pipeline

Run all phases:

```
python run_pipeline.py --phase ALL
```

Run individual phases:

```
python run_pipeline.py --phase A
python run_pipeline.py --phase B
python run_pipeline.py --phase C
python run_pipeline.py --phase D
```

---

## Input Data

### Required

* GWAS data (VCF or summary statistics) placed in:

  ```
  data/raw/
  ```

### Automatically Downloaded

* HapMap3 SNP list
* LD scores (European reference)
* baselineLD annotations
* LDSC regression weights
* ChromHMM segmentation files
* H3K27ac peak data

---

## Outputs

### Processed Data

```
data/processed/
```

* Cleaned GWAS summary statistics
* LDSC-formatted files
* Consensus enhancer regions

### LDSC Results

```
outputs/ldsc/
```

* Heritability estimates (h²)
* Genetic correlation (rg)

### Logs and QC

```
outputs/logs/
```

* Annotation QC summaries
* Execution logs

---

## Methodological Notes

* GWAS data are harmonized to a consistent genome build prior to analysis
* LDSC uses precomputed LD scores and regression weights from the Broad Institute
* Epigenomic annotations are integrated using interval overlap between ChromHMM states and H3K27ac peaks
* All steps are deterministic and reproducible given identical inputs

---

## Reproducibility

To fully reproduce results:

1. Clone the repository
2. Install dependencies
3. Place GWAS data in `data/raw/`
4. Run the pipeline

All intermediate and final outputs will be generated automatically.

---

## Limitations

* Requires careful alignment of genome builds across datasets
* Accuracy depends on quality of input GWAS data
* Epigenomic annotations are dependent on selected reference tissues

---

## Citation

If you use this pipeline, please cite:

```
Author(s). Epigenetic Aging GWAS Pipeline:
An End-to-End Framework for Integrating GWAS, LDSC, and Epigenomic Annotations
in Biological Aging Research. [Year].
```

Additionally, please cite the following tools used within this pipeline:

* Bulik-Sullivan et al., 2015 — LD Score Regression
* Roadmap Epigenomics Consortium — ChromHMM annotations
* ENCODE/Roadmap — H3K27ac datasets

---

## License

This project is released under the MIT License.

---

## Contact

For questions, issues, or collaboration:

* Open an issue in this repository
