from sklearn.cluster import DBSCAN
import numpy as np
import pickle

"""
data = np.load('output_filename.npz', allow_pickle=True)

files = data.files
files.sort()

arr = []

for sequence in files:
    seq = data[sequence]
    arr.append(seq.item().get('avg'))

np_arr = np.array(arr)

np.save("data_sorted.npy", np_arr)

"""

print('loading data')
data = np.load('/ifs/groups/eces450650Grp/ECES450650_SP22/projectE/ESM/for_classifier.npy')

print('clustering data')
#clustering = DBSCAN(eps=0.5, min_samples=10).fit(data)
clustering =DBSCAN().fit(data)

print('saving model')
pickle.dump(clustering, open('models/dbscan_d5_10_ESM.pkl', 'wb'))

