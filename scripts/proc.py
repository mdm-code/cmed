#!/usr/bin/env python

import json
import sys
from med_crawler import sim
import csv
import itertools
from collections import defaultdict
import tqdm


def main() -> None:
    with open(sys.argv[1], "r") as f:
        entries = json.load(f)

    pos_dicts = defaultdict(list)

    for entry in entries:
        for pos in entry["pos"]:
            for form in entry["forms"]:
                k, v = form["regular"], entry["headword"]["regular"]
                pos_dicts[pos["code"]].append((k, v,))

    with open(sys.argv[2], "r") as f:
        forms = [line.strip() for line in f.readlines()]

    with open(sys.argv[4], "w") as out:
        fieldnames = ["form"] + ["lemma", "score"] * 3
        writer = csv.writer(out, delimiter=",", escapechar="\\")
        writer.writerow(fieldnames)

        # Three categories for verbs
        pos = sys.argv[3]

        d_verb = pos_dicts.get("verb", None)
        d_ptp = pos_dicts.get("participle", None)
        d_adj = pos_dicts.get("adjective", None)

        # if d:
        for form in tqdm.tqdm(forms):
            v_verb = sim.extract(form, choices=d_verb, limit=3)
            v_ptp = sim.extract(form, choices=d_ptp, limit=3)
            v_adj = sim.extract(form, choices=d_adj, limit=3)
            row = [form] + \
                list(itertools.chain(*v_verb)) + \
                list(itertools.chain(*v_ptp)) + \
                list(itertools.chain(*v_adj))

            writer.writerow(row)


if __name__ == "__main__":
    main()
