from config import Config
from influxdb import DataFrameClient
import pandas as pd
import numpy as np

class Influx:
    def __init__(self):
        self.config = Config()

    def write_data(self, file, db_name):
        data = "Дата замера"
        df = pd.DataFrame()
        d_temp = pd.read_excel(file, 'АЗС+магазин', parse_dates=[data], index_col=data) 
        df = pd.concat([df, d_temp], ignore_index=False) 

        d_temp = pd.read_excel(file, 'АЗС+магазин (2)', parse_dates=[data], index_col=data) 
        df = pd.concat([df, d_temp], ignore_index=False) 

        d_temp = pd.read_excel(file, 'АЗС+магазин (3)', parse_dates=[data], index_col=data) 
        df = pd.concat([df, d_temp], ignore_index=False) 

        d_temp = pd.read_excel(file, 'АЗС+магазин (4)', parse_dates=[data], index_col=data) 
        df = pd.concat([df, d_temp], ignore_index=False) 

        d_temp = pd.read_excel(file, 'АЗС+магазин (5)', parse_dates=[data], index_col=data) 
        df = pd.concat([df, d_temp], ignore_index=False) 

        df = df.sort_index(ascending=True)

        df_numeric = df.select_dtypes(include=[np.number])
        numeric_cols = df_numeric.columns.values

        for col in numeric_cols:
            missing = df[col].isnull()
            num_missing = np.sum(missing)

            if num_missing > 0: 
                med = df[col].median()
                df[col] = df[col].fillna(med)
        
        host = self.config.INFLUX_HOST
        port = self.config.INFLUX_PORT
        dbname = db_name
        username = self.config.INFLUX_USER
        password = self.config.INFLUX_PASSWORD
        protocol = 'line'
        client = DataFrameClient(host = host, port = port, username = username, password = password, database = dbname)

        client.create_database(dbname)
        client.switch_database(dbname)

        client.write_points(df, measurement='station', batch_size=100000, protocol=protocol)
        print(f'Считаны данные из файла {file} и записаны в InfluxDB в базу {db_name}')

