

import numpy as np
import os
import io
from os.path import isfile, join
import torch
#from tempfile import TemporaryFile


path ="/ifs/groups/eces450650Grp/ECES450650_SP22/projectE/ESM/esm1b-0"

os.chdir(path)

def read_pt_file(file_path):
    output = torch.load(file_path)
    out = output['representations'][33].numpy()
    out = out[0]
    #out = len(output['representations'][33])
    #print(out)
    #yield out
    return out

def get_label(file_path):
    output = torch.load(file_path)
    print(output)
    out = output['label'].split('.')
    outnp = out[0][-1]+"."+out[1]+"."+out[2]+"."+out[3]
    outarr = outnp
    return outarr

embedding = []
label_dict = {}
counter =0
file_count = 0

labels = []
firstTime = True
print(len(os.listdir()))
file_dir = os.listdir()
file_dir.sort()
for file in os.listdir():
    #Check whether file is in the .pt format or not
    if file.endswith(".pt"):
        
        file_path = f"{path}/{file}"

        # call read file function
        #file_embedding = read_pt_file(file_path)
        #embedding.append(file_embedding)
        #if (firstTime == True):
         #   embedding = read_pt_file(file_path)
        key = get_label(file_path)

        #label_dict[key] = counter
        #labels = label_dict[key]
        #counter= counter +1
            
            #size = len(labels)
            #labels = np.chararray((1,size))
        #    firstTime = False
        #else:
         #   row =read_pt_file(file_path)
          #  row1 = get_label(file_path)
            
           # np.append(embedding, row)
            
        if key not in label_dict.keys():
            label_dict[key] = counter
            counter = counter +1
        labels.append(label_dict[key])
        #np.append(labels,label_dict[key])

        file_count = file_count+1
 #       if file_count >5:
  #          break

#print(labels)

path = "/ifs/groups/eces450650Grp/ECES450650_SP22/projectE/ESM"
os.chdir(path)
#print(file_count)
print(embedding.size)
#print(labels.size)
labels_np = np.array(labels)
#np.savez('for_classifier.npz',embedding_np)
#np.save('for_classifier.npy', embedding_np)
np.save('labels.npy', labels_np)
