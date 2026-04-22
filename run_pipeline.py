PHASE_A = [
    ["python", "src/setup/create_structure.py"],
    ["python", "src/setup/runtime_checks.py"],
    ["bash", "scripts/install_system.sh"],
    ["python", "src/reference/download_hm3.py"],
    ["bash", "src/reference/download_ldscores.sh"],
    ["bash", "src/reference/download_baselineLD.sh"],
    ["bash", "src/reference/download_weights.sh"],
    ["python", "src/reference/verify_hashes.py"],
]
