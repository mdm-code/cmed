#!/usr/bin/env python3

import json
import sys


with open(sys.argv[1], "r") as f:
    data = json.load(f)


pos = set()

for entry in data:
    if entry["pos"]:
        pos.add(entry["pos"][0]["expanded"])


for p in pos:
    sys.stdout.write(p+"\n")
