import pandas as pd
import gzip
import glob

def load_bed(file):
    if file.endswith(".gz"):
        f = gzip.open(file, "rt")
    else:
        f = open(file)

    rows = []
    for line in f:
        parts = line.strip().split("\t")
        rows.append([parts[0], int(parts[1]), int(parts[2])])

    return pd.DataFrame(rows, columns=["chr", "start", "end"])


def build_consensus():

    chromhmm_files = glob.glob("refs/chromhmm/*.bed.gz")
    h3k27ac_files = glob.glob("refs/h3k27ac/*.narrowPeak.gz")

    chromhmm_df = pd.concat([load_bed(f) for f in chromhmm_files])
    h3_df = pd.concat([load_bed(f) for f in h3k27ac_files])

    print("ChromHMM regions:", len(chromhmm_df))
    print("H3K27ac regions:", len(h3_df))

    # Simple overlap logic (exact replication would use interval trees)
    merged = pd.merge(chromhmm_df, h3_df, on="chr")

    overlap = merged[
        (merged["start_x"] < merged["end_y"]) &
        (merged["end_x"] > merged["start_y"])
    ]

    consensus = overlap[["chr", "start_x", "end_x"]].drop_duplicates()
    consensus.columns = ["chr", "start", "end"]

    consensus.to_csv("data/processed/consensus_enhancers.bed",
                     sep="\t", index=False, header=False)

    print("Consensus enhancers saved")


if __name__ == "__main__":
    build_consensus()
