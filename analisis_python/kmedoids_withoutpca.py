import pandas as pd
import math
from sklearn.decomposition import PCA
from sklearn import preprocessing
import matplotlib.pyplot as plt
from sklearn_extra.cluster import KMedoids
from sklearn import metrics

features = pd.read_csv('./../Data/specPowerDatamartTransform.csv')
columns=features.columns
#PCA
#dicha funcion scale lo que hace es centrar y escalar los datos
scaled_data=preprocessing.scale(features)
descripcion=features.describe()

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
initial_centroids_desnormalize=[]
for instance in initial_centroids:
    print(instance)
    temp = []
    for i in range(len(instance)):
        media = descripcion[columns[i]]['mean']
        std = descripcion[columns[i]]['std']
        temp.append(round(instance[i] * std + media))
    initial_centroids_desnormalize.append(temp)
    print(temp)

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

#tengo dudas con el 25 y el 34
indices_columnas=[0,1,3,25,34,35,37,38,40]
for k in range(3):
    transactions = []
    indices = []
    print("Exportando cluster para K=",k)
    for i, pred in enumerate(y_kmedoids):
        if pred==k:
            indices.append(i)
    transactions=features.iloc[indices,indices_columnas]
    df=pd.DataFrame(transactions)
    df.to_excel('./ClusteringResult/cluster_kmedoidesk='+str(k)+'.xlsx', index=False)
