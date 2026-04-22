import pandas as pd

def harmonize():
    df = pd.read_csv("data/interim/aging_trait.tsv", sep="\t")

    df["CHR"] = df["CHR"].astype(str)
    df["BP"] = df["BP"].astype(int)

    df["A1"] = df["A1"].str.upper()
    df["A2"] = df["A2"].str.upper()

    df = df.dropna(subset=["BETA", "SE", "P"])

    df.to_csv("data/interim/aging_trait_harmonized.tsv", sep="\t", index=False)

    print("Harmonization complete")

if __name__ == "__main__":
    harmonize()
