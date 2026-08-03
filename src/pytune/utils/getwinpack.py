# Pytune        getwinpack.py
# Author:       Loadrsoftworks
# Description:  Identify windows package (.msi .exe)

from pathlib import Path
import struct

def check_package_type(source_path: str | Path) -> int:
    """
    Inspects a file path or buffer to identify if it is an executable (EXE) or MSI Installer.
    EXE: 1
    MSI: 2
    ERR: 0
    """

    path = Path(source_path)

    try:
        if not path.is_file():
            return "Invalid path or file does not exist"
    except ValueError:
        exit() #Terminate the process

    ext = path.suffix.lower()

    try: 
        with open(path, "rb") as f:
            header = f.read(8)

            # Portable Executable (EXE) magic number: 'MZ'
            if header.startswith(b"MZ"):
                return 1 #EXE

            if header.startswith(b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1"):
                return 2 #MSI

    except IOError:
        return 0 #ERR

    #Fallback - No magic numbers identified but file path is valid
    if ext == ".exe":
        return 1

    if ext == ".msi":
        return 2

    return 0


def inspect_package(source_path: str | Path) -> str:
    """Compatibility wrapper used by the UI layer."""
    package_type = check_package_type(source_path)
    if package_type == 1:
        return "EXE"
    if package_type == 2:
        return "MSI"
    return "Unknown or invalid file"

if __name__ == "__main__":
    sample_file = r"sample.txt"
    print(f"Package Type: {check_package_type(sample_file)}")
