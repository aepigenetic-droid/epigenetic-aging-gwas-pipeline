import subprocess
import os

def munge():

    os.makedirs("data/processed/ldsc", exist_ok=True)

    cmd = [
        "python",
        "refs/ldsc/munge_sumstats.py",
        "--sumstats", "data/processed/aging_trait_clean.tsv",
        "--out", "data/processed/ldsc/aging_trait",
        "--merge-alleles", "refs/hm3/w_hm3.snplist"
    ]

    print("Running munge_sumstats...")
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    munge()
