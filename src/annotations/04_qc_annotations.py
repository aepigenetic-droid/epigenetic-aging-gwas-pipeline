import pandas as pd

def qc():

    df = pd.read_csv("data/processed/consensus_enhancers.bed",
                     sep="\t", header=None)

    df.columns = ["chr", "start", "end"]

    print("Total enhancer regions:", len(df))
    print("Unique chromosomes:", df["chr"].nunique())

    sizes = df["end"] - df["start"]
    print("Mean region size:", sizes.mean())

    df.describe().to_csv("outputs/logs/annotation_qc.csv")

    print("QC complete")


if __name__ == "__main__":
    qc()
