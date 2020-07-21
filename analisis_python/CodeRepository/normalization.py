import shutil
import psycopg2
from psycopg2 import sql
import pandas as pd

spec_power_original_file = '../Data/specPowerDatamartTransform.xlsx'
spec_power_data_transform_file = '../Data/specPowerNormalizationTransform.xlsx'

def normalize(current_value, min_value,max_value):
    min_new_value=0
    max_new_value=1
    return min_new_value+((current_value-min_value)/(max_value-min_value))*(max_new_value-min_new_value)

def parameterNormalization(file_path, parameter):
    reader = pd.read_excel(file_path, header=0)
    column_register = []
    min = float("inf")#representa el valor +infinito
    max = float("-inf")#represente el valor -infinito
    for row in reader[parameter]:
        if row < min:
            min = row
        if row > max:
            max = row
    #print(parameter,"Minimo", min,"Maximo", max,"Iguales",min==max)
    for row in reader[parameter]:
        column_register.append(normalize(row,min,max))
    reader[parameter] = column_register
    reader.to_excel(file_path, index=False)

shutil.copy2(spec_power_original_file, spec_power_data_transform_file)
reader = pd.read_excel(spec_power_data_transform_file, header=0)
columns = reader.columns
for parameter in columns:
    parameterNormalization(spec_power_data_transform_file, parameter)
