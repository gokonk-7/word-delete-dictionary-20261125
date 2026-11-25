#!/bin/sh
# Run the entry program: writes the chosen word to /output/entry.txt
set -e
cd "$(dirname "$0")"
python3 main.py
