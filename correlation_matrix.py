import pandas as pd

spec_power_data_file = 'Data/specPowerDataTransform.xlsx'
reader = pd.read_excel(spec_power_data_file, header=0)
"""
La idea es ir quitando los atributos que estan altamente correlacionados, pues los mismos no aportan
individualmente informacion en el proceso de clasificacion.
"""
print("Matriz de correlacion de Pearson")
print(reader.corr())
#print("Matriz de covarianza")
#print(reader.cov())