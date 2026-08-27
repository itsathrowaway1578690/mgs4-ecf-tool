#!/usr/bin/env python3
"""
Decrypt or re-encrypt MGS4 Master Collection .ecf configuration files.

The transform is symmetric XOR:
- Key: MGS4ConfigFileSecureKey@2024
- 28-byte blocks
- Rotate the key left by one byte for each successive block

Usage:
    python mgs4_ecf_tool.py decrypt mgs4.ecf mgs4.ini
    python mgs4_ecf_tool.py encrypt mgs4.ini mgs4.ecf

"decrypt" and "encrypt" perform the same byte transform; both commands
are provided simply to make the intended operation clear.
"""

from pathlib import Path
import argparse

KEY = b"MGS4ConfigFileSecureKey@2024"

def transform(data: bytes) -> bytes:
    n = len(KEY)
    out = bytearray(len(data))
    for i, value in enumerate(data):
        block = i // n
        offset = i % n
        out[i] = value ^ KEY[(offset + block) % n]
    return bytes(out)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("decrypt", "encrypt"))
    parser.add_argument("input")
    parser.add_argument("output")
    args = parser.parse_args()

    source = Path(args.input)
    destination = Path(args.output)
    destination.write_bytes(transform(source.read_bytes()))
    print(f"{args.mode.title()}ed: {source} -> {destination}")

if __name__ == "__main__":
    main()
