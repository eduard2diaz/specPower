import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn import preprocessing

spec_power_data_file = 'Data/specPowerNormalizationTransform.xlsx'

"""
Los 5 pasos del proceso PCA.
1.Cargar los datos
2.Normalizarlos
3.Obtener los autovectores y autovalores a partir de la matriz de covarianza
4.Seleccionar los autovectores correspondientes a las componentes principales
5.Proyectar el dataset original sobre el nuevo espacio de dimensión < 4
"""
reader = pd.read_excel(spec_power_data_file, header=0)
columns = reader.columns

data_csv=reader._get_values
index=['Sample '+str(ind) for ind in range(1,len(data_csv)+1)]
data=pd.DataFrame(data=data_csv,columns=columns,index=index)
#print(data.shape) Imprimimos la forma(dimensiones) de nuestra matriz
scaled_data=preprocessing.scale(data.T)#como nos damos cuenta estamos pasando la transpuesta,
#dicha funcion scale lo que hace es centrar y escalar los datos
pca=PCA()
pca.fit(scaled_data)#Aqui se hacen los calculos de PCA
pca_data=pca.transform(scaled_data)#Aqui generamos las coordenadas para una grafica de PCA basado en los datos escalados
"""Cada nuevo atributo es una combinacion lineal de los atributos originales. PCA permite describir un conjunto
de datos en termino de nuevas variables no correlacionadas. Dichos componentes se ordenan por la cantidad
de varianza original que describen por la cantidad de varianza original que describen
print(pca_data) """
#calculamos el porcentaje de variacion de cada componente principal
per_var=np.round(pca.explained_variance_ratio_*100,decimals=1)
#creamos los labels, uno por cada compoenente principal
labels=['PC'+str(x) for x in range(1, len(per_var)+1)]
plt.bar(x=range(1,len(per_var)+1),height=per_var,tick_label=labels)
plt.ylabel('Porcentaje de varianza explicada')
plt.xlabel('Componente principal')
plt.title('Screen plot')
plt.show()
#imprimiendo el porcentaje de varianza explicada por cada componente
for x in range(1,len(per_var)):
    print("PC"+str(x), "Percentage", per_var[x-1])

#print(len(pca.components_)) imprime la cantidad de componentes principales con que cuenta
#Ahora analizamos para el primer compoenente principal las 10 muestras mas influyentes
loading_scores=pd.Series(pca.components_[0],index=index)
sorted_loading_scores=loading_scores.abs().sort_values(ascending=False)
top_10=sorted_loading_scores[0:10].index.values
print(loading_scores[top_10])