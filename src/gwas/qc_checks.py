import pandas as pd
import numpy as np

def qc():
    df = pd.read_csv("data/interim/aging_trait_harmonized.tsv", sep="\t")

    print("Rows:", len(df))

    print("NaN counts:")
    print(df.isna().sum())

    print("P-value range:", df["P"].min(), df["P"].max())

    print("Effect size range:", df["BETA"].min(), df["BETA"].max())

    print("QC complete")

if __name__ == "__main__":
    qc()
