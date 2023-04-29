data=pd.read_csv('data.csv')
result=pd.read_csv('result.csv',skiprows=7)
labels = pd.read_csv('labels.csv', header=None, names=['contigname', 'cluster'])
output=pd.concat([data,result],axis=1) 
output = output.merge(labels, how='inner', on='contigname') # 107w row
ari = adjusted_rand_score(output['The clustering results:'], output['cluster'])
print(ari)