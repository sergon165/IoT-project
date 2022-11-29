from config import Config
from influx import Influx


def main():
    inp = ''
    while inp != '0':
        print('\nМеню')
        print('1. Записать данные в InfluxDB')
        print('2. Удалить базу данных')
        print('Для выхода введите 0.\n')

        inp = input('Выберите пункт меню: ')
        if inp == '1':
            file = input('Путь к исходному файлу (../raw_data/GAS.xlsx): ')
            if file == '':
                file = '../raw_data/GAS.xlsx'
            db_name = input('Название базы данных: ')
            influx.write_data(file, db_name)
        elif inp == '2':
            db_name = input('Название базы данных: ')
            print('Данные удалены')


if __name__ == '__main__':
    config = Config()
    influx = Influx()
    main()
