#!/bin/bash

# Find all files excluding specific directories and the output file, extract http links, and save to links.txt
find . \( -path "./docs_env" -o -path "./venv" \) -prune -o -type f ! -name "links.txt" -exec grep -Eo 'http[^"]+' {} + > links.txt

# Extract links containing 'github' into GitHub.txt
grep "github" links.txt > GitHub.txt
