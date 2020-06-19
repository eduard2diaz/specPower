import pandas as pd

spec_power_data_file = 'Data/specPowerDataTransform.xlsx'
covariance_matrix_data_file = 'Data/covariance_matrix.xlsx'
"""
Los 5 pasos del proceso PCA.
1.Cargar los datos
2.Normalizarlos
3.Obtener los autovectores y autovalores a partir de la matriz de covarianza
4.Seleccionar los autovectores correspondientes a las componentes principales
5.Proyectar el dataset original sobre el nuevo espacio de dimensión < 4
"""
reader = pd.read_excel(spec_power_data_file, header=0)

covariance_matrix=reader.cov()
print("Matriz de covarianza")
print(covariance_matrix)
df=pd.DataFrame(covariance_matrix)
df.to_excel(covariance_matrix_data_file, index=False)

