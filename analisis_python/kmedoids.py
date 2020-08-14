import pandas as pd
from sklearn.decomposition import PCA
from sklearn import preprocessing
import matplotlib.pyplot as plt
from sklearn_extra.cluster import KMedoids
from sklearn import metrics


features = pd.read_csv('./../Data/specPowerDatamartTransform.csv')
#PCA
#dicha funcion scale lo que hace es centrar y escalar los datos
scaled_data=preprocessing.scale(features)

#Planteamos los datos como la relacion lineal de solamente dos componentes
pca = PCA(n_components = 2)
dataset_questions_pca = pca.fit_transform(scaled_data)

#Analizamos la cantidad de cluster a partir de la informacion obtenida de la relacion lineal del pca
#Aplico el metodo del codo sobre el conjunto de datos
wcss = []
for i in range(1, 7):
    kmedoids = KMedoids(n_clusters = i, random_state = 0)
    kmedoids.fit(dataset_questions_pca)
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
y_kmedoids = kmedoids.fit_predict(dataset_questions_pca)
initial_centroids=kmedoids.cluster_centers_

print("Centroides iniciales")
for instance in initial_centroids:
    print(instance)

silhouette_avg = metrics.silhouette_score(scaled_data, y_kmedoids)
print ('El coeficiente de silueta del agrupamiento es = ', silhouette_avg)


plt.scatter(dataset_questions_pca[y_kmedoids == 0, 0], dataset_questions_pca[y_kmedoids == 0, 1], c = 'red', label = 'Cluster 1')
plt.scatter(dataset_questions_pca[y_kmedoids == 1, 0], dataset_questions_pca[y_kmedoids == 1, 1], c = 'blue', label = 'Cluster 2')
plt.scatter(dataset_questions_pca[y_kmedoids == 2, 0], dataset_questions_pca[y_kmedoids == 2, 1], c = 'green', label = 'Cluster 3')
plt.scatter(kmedoids.cluster_centers_[:, 0], kmedoids.cluster_centers_[:, 1], c = 'yellow', label = 'Centroides')
plt.title('Ploteo K-Medoides')
plt.xlabel('PCA 1')
plt.ylabel('PCA 2')
plt.legend()
plt.show()
