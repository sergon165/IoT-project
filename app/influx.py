from config import Config
from influxdb import DataFrameClient


class Influx:
    def __init__(self):
        self.config = Config()

    def write_data(self, file, db_name):
        print(f'Считаны данные из файла {file} и записаны в InfluxDB в базу {db_name}')

