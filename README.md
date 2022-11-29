# Проект IoT

## Участники
- Гончаров Сергей
- Катаев Юрий
- Чирков Дмитрий

## Установка и запуск
### Docker
1. Установить Docker с [официального сайта](https://www.docker.com/) и запустить
2. Запустить терминал и перейти в директорию проекта
3. Выполнить команду
```
docker-compose up -d
```
4. Для остановки использовать (из директории проекта)
```
docker-compose down
```
### Python
#### Установка зависимостей

Для Windows
```
cd app &&\
python -m venv venv &&\
venv\Scripts\activate.bat &&\
pip install -r requirements.txt &&\
deactivate
```
Для Linux и MacOS
```
cd app &&\
python3 -m venv venv &&\
source venv/bin/activate &&\
pip install -r requirements.txt &&\
deactivate
```
#### Запуск
```
python main.py
---- или ----
python3 main.py
```