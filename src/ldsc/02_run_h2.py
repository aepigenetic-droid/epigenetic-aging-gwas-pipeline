import subprocess
import os

def run_h2():

    os.makedirs("outputs/ldsc", exist_ok=True)

    cmd = [
        "python",
        "refs/ldsc/ldsc.py",
        "--h2", "data/processed/ldsc/aging_trait.sumstats.gz",
        "--ref-ld-chr", "refs/ldsc/eur_w_ld_chr/",
        "--w-ld-chr", "refs/ldsc/weights/weights_hm3_no_hla/",
        "--out", "outputs/ldsc/aging_trait_h2"
    ]

    print("Running LDSC heritability...")
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    run_h2()
