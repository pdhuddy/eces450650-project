from sklearn.cluster import AgglomerativeClustering
import numpy as np
import pickle

print('loading data')
data = np.load('/ifs/groups/eces450650Grp/ECES450650_SP22/projectE/ESM/for_classifier.npy')

print('clustering data')
#clustering = AgglomerativeClustering(n_clusters=2027).fit(data)
clustering = AgglomerativeClustering(n_clusters=316,affinity='cosine',linkage='average').fit(data)


print('saving model')
pickle.dump(clustering, open('models/hier_euc_ESM_cos.pkl', 'wb'))

