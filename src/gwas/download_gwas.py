import os
import pandas as pd
import urllib.request

def download():
    df = pd.read_csv("config/traits.csv")

    os.makedirs("data/raw", exist_ok=True)

    for _, row in df.iterrows():
        if row["source"] == "url":
            url = row["file"]
            out = f"data/raw/{row['trait']}.vcf.gz"
            print("Downloading:", url)
            urllib.request.urlretrieve(url, out)

    print("GWAS download complete")

if __name__ == "__main__":
    download()
