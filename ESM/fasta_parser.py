#!/usr/bin/env python3 -u

import math
fasta_file = "/ifs/groups/eces450650Grp/data/incremental_data/engineered/batch-0.fasta"

def parse_fasta(fname):
    with open(fname, "r") as fh:

        lines = fh.readlines()

        #Create veriables for storing the identifies and the sequence
        identifier = None
        sequence = []
        labels = []
        seq_num = 0
        

        for line in lines:
            line = line.strip(); #Remove trailing newline characters
            if line.startswith(">"):
                newline = line.split(" ")
                newline =  newline[0]+newline[1]
                prev_label = newline
                
                if (len(lines[seq_num+1]) > 0) and (len(lines[seq_num+1])<1024):
                    seq_num = seq_num + 1
                    yield newline
                else:
                    pass

                
            else:
                seq_num = seq_num +1
                #if len(line) > 0:
                 #   if len(line) > 1024:
                  #      str_len = len(line)
                   #     num_increments = math.floor(str_len/1024)
                    #    seq_num = seq_num + 1
                    #    for iter in range(0,num_increments+1):
                     #       newheader = prev_label+"_"+ f"{iter}"
                      #      segment = line[iter*1024:1024*(iter+1)].upper()
                            #print("SEGMENT: " + f"{iter}\n")
                            #print(segment)
                            #print("SEGMENT LENGTH: " + f"{len(segment)}")
                       #     line1 = newheader + "\n" + segment
                        #    yield line1
                    #else:
                     #   seq_num = seq_num + 1
                line = line.upper()
                yield line
                
                

for entry in parse_fasta(fasta_file):
    print(entry)
