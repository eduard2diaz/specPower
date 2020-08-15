import pandas as pd
from sklearn.decomposition import PCA
from sklearn import preprocessing
import matplotlib.pyplot as plt
from sklearn_extra.cluster import KMedoids
from sklearn import metrics
import psycopg2
from psycopg2 import sql

connection = psycopg2.connect(host="localhost", database="specPower", user="postgres", password="postgres")
# Creamos el cursor con el objeto conexion
cur = connection.cursor()

features = pd.read_csv('./../Data/specPowerDatamartTransform.csv')
columnas=features.columns
spec_power_parameters = [
    {
        'name': 'Hardware Vendor',
        'table': 'hardware_vendor'
    },
    {
        'name': 'Processor',
        'table': 'processor'
    },
    {
        'name': 'Power Supply Details',
        'table': 'power_supply_details'
    },
]

def createDataDic(file_path, parameter,db_cursor):
    reader = pd.read_excel(file_path, header=0)
    column_register = []

    for row in reader[parameter['name']]:
        db_cursor.execute("select name from "+parameter['table']+" where id="+str(row))
        result=db_cursor.fetchone()
        column_register.append(result[0])
    reader[parameter['name']] = column_register
    reader.to_excel(file_path, index=False)

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
        media = descripcion[columnas[i]]['mean']
        std = descripcion[columnas[i]]['std']
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
    name = './ClusteringResult/cluster_kmedoidesk=' + str(k) + '.xlsx'
    df.to_excel(name, index=False)
    for parameter in spec_power_parameters:
        createDataDic(name, parameter, cur)

#Filtrando campos interesantes de los centroides iniciales
fields_filters=[]
for instance in initial_centroids_desnormalize:
    temp=[]
    for i in range(len(instance)):
        if i in indices_columnas:
            temp.append({columnas[i]:instance[i]})
    print(temp)
    fields_filters.append(temp)
