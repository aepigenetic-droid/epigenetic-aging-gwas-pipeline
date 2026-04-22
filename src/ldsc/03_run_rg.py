import subprocess

def run_rg():

    cmd = [
        "python",
        "refs/ldsc/ldsc.py",
        "--rg",
        "data/processed/ldsc/aging_trait.sumstats.gz,data/processed/ldsc/aging_trait.sumstats.gz",
        "--ref-ld-chr", "refs/ldsc/eur_w_ld_chr/",
        "--w-ld-chr", "refs/ldsc/weights/weights_hm3_no_hla/",
        "--out", "outputs/ldsc/aging_trait_rg"
    ]

    print("Running LDSC genetic correlation...")
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    run_rg()
