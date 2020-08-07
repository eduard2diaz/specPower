import pandas as pd

spec_power_data_file = './../Data/specPowerDatamartTransform.xlsx'
correlation_matrix_data_file = './Preprocessing/specPowerCorrelationMatrix.xlsx'
reader = pd.read_excel(spec_power_data_file, header=0)
print("Matriz de correlacion de Pearson")
correlation_matrix=reader.corr()
print(correlation_matrix)
df=pd.DataFrame(correlation_matrix)
df.to_excel(correlation_matrix_data_file, index=False)
