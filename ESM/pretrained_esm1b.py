#!/usr/bin/env python3 -u

import torch
import esm

def dataLoader(fname):
    data = []
    #(label, sequence)
    with open(fname, "r") as fh:
        lines = fh.readlines()
        label = ""
        sequence =""
        seq_num = 0

        for line in lines:
            if line.startswith(">"):
                label = line.split(">")[1]
                label = label.rstrip()
                label = f"{label}"
                sequence = lines[seq_num+1].rstrip()
                sequence = f"{sequence}"
                seq_num = seq_num+1
                data.append((label,sequence))
    print(data)
    return data



def main(data):
    #Load ESM-1b model
    model, alphabet = esm.pretrained.esm1b_t33_650M_UR50S()
    batch_converter = alphabet.get_batch_converter()
    model.eval()

    #Prepare data
    #data = dataLoader(input_file)

    batch_labels,batch_strs = batch_converter(data)
    
    #Extract per-residue representations (on CPU)
    with torch.no_grad():
        results = model(batch_tokens, repr_layers=[33], return_contacts=True)

    token_representations = results["representations"][33]

    #Generate per-sequence representations via averaging
    # NOTE: token 0 is always beginning-of-sequence token, so the first residue is token 1
    sequence_representations =[]
    for i, (_, seq) in enumerate(data):
        sequence_representations.append(token_representations[i,1:len(seq)+1].mean(0))

    return sequence_representations
    #return 0

if __name__ == "__main__":
    input_file = "parsed.fasta"
    data = dataLoader(input_file)
    #print(data)
    reps = main(data)
    print(reps)

