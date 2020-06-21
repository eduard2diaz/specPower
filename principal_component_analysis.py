import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn import preprocessing

spec_power_data_file = 'Data/specPowerNormalizationTransform.xlsx'
covariance_matrix_data_file = 'Data/specPowerCovarianceMatrix.xlsx'
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
# print(reader.tail(8)) retorna las ultimas 8 filas

covariance_matrix = reader.cov()
# print("Matriz de covarianza")
# print(covariance_matrix)
df = pd.DataFrame(covariance_matrix)
df.to_excel(covariance_matrix_data_file, index=False)

data_csv=reader._get_values
index=['Muestra '+str(ind) for ind in range(len(data_csv))]
data=pd.DataFrame(data=data_csv,columns=columns,index=index)
scaled_data=preprocessing.scale(data.T)#como nos damos cuenta estamos pasando la transpuesta
pca=PCA()
pca.fit(scaled_data)
pca_data=pca.transform(scaled_data)
print(pca_data)
"""
per_var=np.round(pca.explained_variance_ratio_*100,decimals=1)
labels=[columns[x-1] for x in range(1, len(per_var)+1)]
plt.bar(x=range(1,len(per_var)+1),height=per_var,tick_label=labels)
plt.ylabel('Porcentaje de varianza explicada')
plt.xlabel('Componente principal')
plt.title('Screen plot')
plt.show()

loading_scores=pd.Series(pca.components_[0])
sorted_loading_scores=loading_scores.abs().sort_values(ascending=False)
top_10=sorted_loading_scores[0:10]

print(loading_scores[top_10])"""