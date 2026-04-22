import subprocess
import sys
from pathlib import Path


# ================================
# HELPER FUNCTION
# ================================
def run_step(step):
    print("\nRunning:", " ".join(step))
    try:
        subprocess.run(step, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Step failed: {step}")
        sys.exit(1)


# ================================
# PHASE A: SETUP + REFERENCES
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
# ================================
# MAIN EXECUTION
# ================================
def main():
    print("\nStarting pipeline...\n")

    # Ensure we are at project root
    project_root = Path(__file__).resolve().parent
    print(f"Project root: {project_root}")

    # Run Phase A
    print("\n=== Phase A: Setup and Reference Data ===")
    for step in PHASE_A:
        run_step(step)

    print("\nPhase A completed successfully.")
    print("\n=== Phase B: GWAS Processing ===")
    for step in PHASE_B:
        run_step(step)

# ================================
# ENTRY POINT
# ================================
if __name__ == "__main__":
    main()
