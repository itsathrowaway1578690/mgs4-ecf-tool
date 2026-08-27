#!/usr/bin/env python3

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
