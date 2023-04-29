import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

data = pd.read_csv('data.csv')
labels = pd.read_csv('labels.csv', header=None, names=['contigname', 'cluster'])
data = data.merge(labels, how='left', on='contigname')

Y=np.array(data.iloc[:,-1])
X = np.array(data.iloc[:,1:-1])

kmeans = KMeans(n_clusters=745, random_state=2023)
kmeans.fit(X)
y_pred = kmeans.predict(X)
row_num=data[data['cluster'].notna()].index

ari = adjusted_rand_score(Y[row_num], y_pred[row_num])
print("ARI score:", ari)