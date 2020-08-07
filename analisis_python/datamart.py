import shutil
import psycopg2
from psycopg2 import sql
import pandas as pd

connection = psycopg2.connect(host="localhost", database="specPower", user="postgres", password="postgres")
# Creamos el cursor con el objeto conexion
cur = connection.cursor()

spec_power_original_file = './../Data/specPowerOriginalDataTemp.xlsx'
spec_power_data_transform_file = './../Data/specPowerDatamartTransform.xlsx'
spec_power_parameters = [
    {
        'name': 'Hardware Vendor',
        'table': 'hardware_vendor'
    },
    {
        'name': 'Form Factor',
        'table': 'form_factor'
    },
    {
        'name': 'Processor',
        'table': 'processor'
    },
    {
        'name': 'DIMMS',
        'table': 'dimms'
    },
    {
        'name': 'Power Supply Details',
        'table': 'power_supply_details'
    },
]

def createDataDic(file_path, parameter, db_cursor):
    db_cursor.execute(
        sql.SQL("delete from {}")
            .format(sql.Identifier(parameter['table'])))

    reader = pd.read_excel(file_path, header=0)
    data_collection_names = []
    data_collection_id = []
    data_collection_counter = 1
    column_register = []

    for row in reader[parameter['name']]:
        if not row in data_collection_names:
            data_collection_names.append(row)
            data_collection_id.append(data_collection_counter)
            primary_id = data_collection_counter
            data_collection_counter += 1
        else:
            primary_id = data_collection_id[data_collection_names.index(row)]
        column_register.append(primary_id)

    reader[parameter['name']] = column_register
    reader.to_excel(file_path, index=False)

    for obj in range(data_collection_id.__len__()):
        db_cursor.execute(
            sql.SQL("insert into {} values (%s, %s)")
            .format(sql.Identifier(parameter['table'])),
            [data_collection_id[obj], data_collection_names[obj]])

shutil.copy2(spec_power_original_file, spec_power_data_transform_file)
for parameter in spec_power_parameters:
    createDataDic(spec_power_data_transform_file, parameter, cur)
connection.commit()
cur.close()
connection.close()
