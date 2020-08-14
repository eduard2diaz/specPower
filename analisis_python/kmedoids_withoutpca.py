import pandas as pd
from sklearn.decomposition import PCA
from sklearn import preprocessing
import matplotlib.pyplot as plt
from sklearn_extra.cluster import KMedoids
from sklearn import metrics

def inspect(results):
    rh          = [tuple(result[2][0][0]) for result in results]
    lh          = [tuple(result[2][0][1]) for result in results]
    supports    = [result[1] for result in results]
    confidences = [result[2][0][2] for result in results]
    lifts       = [result[2][0][3] for result in results]
    return list(zip(rh, lh, supports, confidences, lifts))

features = pd.read_csv('./../Data/specPowerDatamartTransform.csv')
features_data = features.values
#PCA
#dicha funcion scale lo que hace es centrar y escalar los datos
scaled_data=preprocessing.scale(features)

#Analizamos la cantidad de cluster a partir de la informacion obtenida de la relacion lineal del pca
#Aplico el metodo del codo sobre el conjunto de datos
wcss = []
for i in range(1, 7):
    kmedoids = KMedoids(n_clusters = i, random_state = 0)
    kmedoids.fit(scaled_data)
    sse=kmedoids.inertia_
    print("Clusters",i,"SSE",sse)
    wcss.append(sse)
plt.plot(range(1, 7), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

#Aplico k-means sobre el conjunto brindado por pca
kmedoids = KMedoids(n_clusters = 3, random_state=0)
y_kmedoids = kmedoids.fit_predict(scaled_data)
initial_centroids=kmedoids.cluster_centers_
etiquetas=kmedoids.labels_

print("Centroides iniciales")
for instance in initial_centroids:
    print(instance)
print("Resumen de agrupamiento")
for i,pred in enumerate(y_kmedoids):
    print("Muestra",i,"se encuentra en ",pred)

silhouette_avg = metrics.silhouette_score(scaled_data, y_kmedoids)
print ('El coeficiente de silueta del agrupamiento es = ', silhouette_avg)

#Planteamos los datos como la relacion lineal de solamente dos componentes
modelo_pca = PCA(n_components = 2)
dataset_questions_pca = modelo_pca.fit(scaled_data)
pca=modelo_pca.transform(scaled_data)
centroides_pca=modelo_pca.transform(initial_centroids)
colores=['blue','red','green']
colores_cluster=[colores[etiquetas[i]] for i in range(len(pca))]

plt.scatter(pca[:,0],pca[:,1],c=colores_cluster,marker='o',alpha=0.4)
plt.scatter(centroides_pca[:,0],centroides_pca[:,1],marker='x',s=100,linewidths=3,c=colores)

xvector=modelo_pca.components_[0]*max(pca[:,0])
yvector=modelo_pca.components_[1]*max(pca[:,1])
columas=features.columns
plt.show()

from apyori import apriori
transactions=[]
indices=[]
for k in range(1):
    transactions.clear()
    indices.clear()
    print("REALIZANDO CLUSTER PARA K=",k)
    for i, pred in enumerate(y_kmedoids):
        if pred==k:
            indices.append(i)
    transactions=features.iloc[indices]
    print("Realizando Apriori para ",len(transactions),"elementos")
    rules = apriori(transactions, min_support = 0.1, min_confidence = 0.6, min_lift = 3, min_length = 2)
    results=list(rules)
    resultDataFrame = pd.DataFrame(inspect(results),columns=['rhs', 'lhs', 'support', 'confidence', 'lift'])
    print(resultDataFrame)
    print("Finaliza Apriori PARA K=",k)
