import pandas as pd

spec_power_data_file = 'Data/specPowerNormalizationTransform.xlsx'
correlation_matrix_data_file = 'Data/specPowerCorrelationMatrix.xlsx'
reader = pd.read_excel(spec_power_data_file, header=0)
"""
La idea es ir quitando los atributos que estan altamente correlacionados, pues los mismos no aportan
individualmente informacion en el proceso de clasificacion.
"""
print("Matriz de correlacion de Pearson")
correlation_matrix=reader.corr()
print(correlation_matrix)
df=pd.DataFrame(correlation_matrix)
df.to_excel(correlation_matrix_data_file, index=False)
