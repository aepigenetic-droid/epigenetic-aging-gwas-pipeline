import gzip
import pandas as pd

def convert_vcf(vcf_path, out_path):
    rows = []

    with gzip.open(vcf_path, "rt") as f:
        for line in f:
            if line.startswith("#"):
                continue

            parts = line.strip().split("\t")

            chrom = parts[0]
            pos = parts[1]
            snp = parts[2]
            ref = parts[3]
            alt = parts[4]
            info = parts[7]

            beta = None
            se = None
            pval = None

            for field in info.split(";"):
                if field.startswith("BETA="):
                    beta = field.split("=")[1]
                elif field.startswith("SE="):
                    se = field.split("=")[1]
                elif field.startswith("P="):
                    pval = field.split("=")[1]

            rows.append([chrom, pos, snp, ref, alt, beta, se, pval])

    df = pd.DataFrame(rows, columns=[
        "CHR", "BP", "SNP", "A1", "A2", "BETA", "SE", "P"
    ])

    df.to_csv(out_path, sep="\t", index=False)

    print("Converted:", out_path)


if __name__ == "__main__":
    convert_vcf(
        "data/raw/aging_trait.vcf.gz",
        "data/interim/aging_trait.tsv"
    )
