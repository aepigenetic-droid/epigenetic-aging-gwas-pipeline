import pandas as pd
import re

def parse_h2():

    file = "outputs/ldsc/aging_trait_h2.log"

    with open(file) as f:
        lines = f.readlines()

    results = {}

    for line in lines:
        if "Total Observed scale h2" in line:
            results["h2"] = float(line.split(":")[1].strip().split()[0])
        if "Lambda GC" in line:
            results["lambda_gc"] = float(line.split(":")[1].strip())

    df = pd.DataFrame([results])
    df.to_csv("outputs/ldsc/h2_results.csv", index=False)

    print("Parsed h2 results")


def parse_rg():

    file = "outputs/ldsc/aging_trait_rg.log"

    with open(file) as f:
        text = f.read()

    matches = re.findall(r"rg:\s+([-\d\.]+)", text)

    df = pd.DataFrame({"rg": matches})
    df.to_csv("outputs/ldsc/rg_results.csv", index=False)

    print("Parsed rg results")


if __name__ == "__main__":
    parse_h2()
    parse_rg()
