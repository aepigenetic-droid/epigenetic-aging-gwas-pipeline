import subprocess
import sys
from pathlib import Path
import argparse
import datetime


# ================================
# HELPER FUNCTIONS
# ================================
def run_step(step):
    print("\nRunning:", " ".join(step))
    try:
        subprocess.run(step, check=True)
    except subprocess.CalledProcessError:
        print(f"Step failed: {step}")
        sys.exit(1)


def run_phase(phase_name, steps):
    print(f"\n=== {phase_name} ===")
    for step in steps:
        run_step(step)
    print(f"\n{phase_name} completed.")


# ================================
# PHASE DEFINITIONS
# ================================
PHASE_A = [
    ["python", "src/setup/create_structure.py"],
    ["python", "src/setup/runtime_checks.py"],
    ["bash", "scripts/install_system.sh"],
    ["python", "src/reference/download_hm3.py"],
    ["bash", "src/reference/download_ldscores.sh"],
    ["bash", "src/reference/download_baselineLD.sh"],
    ["bash", "src/reference/download_weights.sh"],
    ["python", "src/reference/verify_hashes.py"],
]

PHASE_B = [
    ["python", "src/gwas/traits_metadata.py"],
    ["python", "src/gwas/download_gwas.py"],
    ["python", "src/gwas/vcf_to_tsv.py"],
    ["python", "src/gwas/harmonize_sumstats.py"],
    ["python", "src/gwas/qc_checks.py"],
    ["python", "src/gwas/allele_standardization.py"],
    ["python", "src/gwas/filter_snps.py"],
    ["python", "src/gwas/validate_sumstats.py"],
]

PHASE_C = [
    ["bash", "scripts/install_ldsc.sh"],
    ["python", "src/ldsc/01_munge_sumstats.py"],
    ["python", "src/ldsc/02_run_h2.py"],
    ["python", "src/ldsc/03_run_rg.py"],
    ["python", "src/ldsc/04_parse_ldsc_logs.py"],
]

PHASE_D = [
    ["bash", "src/annotations/01_download_chromhmm.sh"],
    ["bash", "src/annotations/02_download_h3k27ac.sh"],
    ["python", "src/annotations/03_build_consensus.py"],
    ["python", "src/annotations/04_qc_annotations.py"],
]

ALL_PHASES = {
    "A": ("Phase A: Setup and Reference Data", PHASE_A),
    "B": ("Phase B: GWAS Processing", PHASE_B),
    "C": ("Phase C: LDSC Analysis", PHASE_C),
    "D": ("Phase D: Epigenomic Annotations", PHASE_D),
}


# ================================
# MAIN EXECUTION
# ================================
def main():

    parser = argparse.ArgumentParser(description="Run pipeline phases")
    parser.add_argument(
        "--phase",
        choices=["A", "B", "C", "D", "ALL"],
        default="ALL",
        help="Select phase to run"
    )
    args = parser.parse_args()

    print("\nStarting pipeline...")
    print("Timestamp:", datetime.datetime.now())

    project_root = Path(__file__).resolve().parent
    print("Project root:", project_root)

    if args.phase == "ALL":
        for key in ["A", "B", "C", "D"]:
            name, steps = ALL_PHASES[key]
            run_phase(name, steps)
    else:
        name, steps = ALL_PHASES[args.phase]
        run_phase(name, steps)

    print("\nPipeline finished successfully.")


# ================================
# ENTRY POINT
# ================================
if __name__ == "__main__":
    main()
