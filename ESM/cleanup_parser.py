#!/usr/bin/env python3 -u

import math
input_file = "parsed.fasta"

def parse_output(fname):
    with open(fname, "r") as fh:

        lines = fh.readlines()

        #Create variables for storing the identifiers and the sequence
        seq_num = 0

        for line in lines:
            if line.startswith(">"):
                if not (lines[seq_num +1].startswith(">")):
                    seq_num=seq_num+1
                    yield line
            else:
                seq_num=seq_num+1
                yield line

for entry in parse_output(input_file):
    print(entry)
