import hashlib
from pathlib import Path

def file_hash(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def verify():
    base = Path("refs")
    for file in base.rglob("*"):
        if file.is_file():
            print(f"{file}: {file_hash(file)[:16]}...")

if __name__ == "__main__":
    verify()
