import os
import urllib.request

def download_hm3():
    os.makedirs("refs/hm3", exist_ok=True)

    url = "https://data.broadinstitute.org/alkesgroup/LDSCORE/w_hm3.snplist.bz2"
    out = "refs/hm3/w_hm3.snplist.bz2"

    urllib.request.urlretrieve(url, out)

    print("Downloaded HM3 snplist")

if __name__ == "__main__":
    download_hm3()
