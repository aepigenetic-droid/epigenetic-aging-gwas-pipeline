import pandas as pd

def standardize():
    df = pd.read_csv("data/interim/aging_trait_harmonized.tsv", sep="\t")

    valid = ["A", "C", "G", "T"]

    df = df[df["A1"].isin(valid) & df["A2"].isin(valid)]

    df.to_csv("data/interim/aging_trait_standardized.tsv", sep="\t", index=False)

    print("Allele standardization complete")

if __name__ == "__main__":
    standardize()
