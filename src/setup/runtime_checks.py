import sys
import shutil
import subprocess

def check_python():
    print("Python version:", sys.version)

def check_tool(tool):
    path = shutil.which(tool)
    if path:
        print(f"{tool} found at {path}")
    else:
        print(f"{tool} NOT found")

def check_r():
    try:
        subprocess.run(["Rscript", "--version"], check=True)
        print("Rscript available")
    except:
        print("Rscript NOT available")

def run_checks():
    check_python()
    check_tool("wget")
    check_tool("curl")
    check_tool("gunzip")
    check_r()

if __name__ == "__main__":
    run_checks()
