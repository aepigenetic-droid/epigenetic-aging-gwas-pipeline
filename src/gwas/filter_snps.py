import pandas as pd

def filter_snps():
    df = pd.read_csv("data/interim/aging_trait_standardized.tsv", sep="\t")

    df = df[df["P"] > 0]
    df = df[df["SE"] > 0]

    df = df[df["A1"] != df["A2"]]

    df.to_csv("data/processed/aging_trait_clean.tsv", sep="\t", index=False)

    print("Filtering complete")

if __name__ == "__main__":
    filter_snps()
