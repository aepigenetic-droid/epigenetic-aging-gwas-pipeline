import pandas as pd

def validate():
    df = pd.read_csv("data/processed/aging_trait_clean.tsv", sep="\t")

    required = ["CHR", "BP", "SNP", "A1", "A2", "BETA", "SE", "P"]

    for col in required:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")

    print("Final dataset shape:", df.shape)

    print("Validation passed")

if __name__ == "__main__":
    validate()
