import pandas as pd

def get_traits():
    traits = [
        {
            "trait": "aging_trait",
            "source": "local",
            "file": "data/raw/aging_trait.vcf.gz",
            "build": "GRCh37",
            "sample_size": 50000
        }
    ]

    df = pd.DataFrame(traits)
    df.to_csv("config/traits.csv", index=False)

    print("Saved traits metadata")

if __name__ == "__main__":
    get_traits()
