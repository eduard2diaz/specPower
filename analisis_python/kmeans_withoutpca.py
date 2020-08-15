import pandas as pd
from sklearn.decomposition import PCA
from sklearn import preprocessing
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics

features = pd.read_csv('./../Data/specPowerDatamartTransform.csv')
columnas=features.columns
descripcion=features.describe()
#PCA
#dicha funcion scale lo que hace es centrar y escalar los datos
scaled_data=preprocessing.scale(features)
print(scaled_data)

#Analizamos la cantidad de cluster a partir de la informacion obtenida de la relacion lineal del pca
#Aplico el metodo del codo sobre el conjunto de datos
wcss = []
for i in range(1, 7):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans.fit(scaled_data)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 7), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

#Aplico k-means sobre el conjunto brindado por pca
kmeans = KMeans(n_clusters = 3, init = 'k-means++',max_iter=300,n_init=10,random_state=1)
y_kmeans = kmeans.fit_predict(scaled_data)
initial_centroids=kmeans.cluster_centers_
etiquetas=kmeans.labels_

print("Centroides iniciales")
initial_centroids_desnormalize=[]
for instance in initial_centroids:
    print(instance)
    temp = []
    for i in range(len(instance)):
        media = descripcion[columnas[i]]['mean']
        std = descripcion[columnas[i]]['std']
        temp.append(round(instance[i] * std + media))
    initial_centroids_desnormalize.append(temp)
    print(temp)

print("Resumen de agrupamiento")
for i,pred in enumerate(y_kmeans):
    print("Muestra",i,"se encuentra en ",pred)

silhouette_avg = metrics.silhouette_score(scaled_data, y_kmeans)
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
plt.show()


#tengo dudas con el 25 y el 34
indices_columnas=[0,1,3,25,34,35,37,38,40]
for k in range(3):
    transactions = []
    indices = []
    print("Exportando cluster para K=",k)
    for i, pred in enumerate(y_kmeans):
        if pred==k:
            indices.append(i)
    transactions=features.iloc[indices,indices_columnas]
    df=pd.DataFrame(transactions)
    df.to_excel('./ClusteringResult/cluster_kmeansk='+str(k)+'.xlsx', index=False)

#Filtrando campos interesantes de los centroides iniciales
for instance in initial_centroids_desnormalize:
    temp=[]
    for i in range(len(instance)):
        if i in indices_columnas:
            temp.append({columnas[i]:instance[i]})
    print(temp)
