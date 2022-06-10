import numpy as np
from Bio import SeqIO

#data = np.load('output_filename.npz', allow_pickle=True)
data =np.load('/ifs/groups/eces450650Grp/ECES450650_SP22/projectE/ESM/labels.npy', allow_pickle=True)
fasta_dict = SeqIO.to_dict(SeqIO.parse(open('../TAPE/batch-0-cap.fasta'), 'fasta'))

labels_dict = {}
labels_arr = []
#files = data.files
data.sort()
#print(data.files)
label_count = 0
#for seq_id in files:
for seq_id in data:
    f = fasta_dict[seq_id]
    family = f.description.split()[1]

    if family not in labels_dict.keys():
        labels_dict[family] = label_count
        label_count += 1

    labels_arr.append(labels_dict[family])

np.save("labels_ESM.npy", labels_arr)

