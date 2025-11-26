import pymysql.cursors
import yaml
from pathlib import Path

class MySQLConnector:
    def __init__(self):
        config_path = Path(__file__).resolve().parent.parent.parent / 'config' / 'app.yml'

        try:
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)['DATABASE']
        except FileNotFoundError:
            raise Exception(f"Помилка: файл конфігурації не знайдено за шляхом: {config_path}")

        self.connection_config = {
            'host': config['HOST'],
            'user': config['USER'],
            'password': config['PASSWORD'],
            'database': config['NAME'],
            'cursorclass': pymysql.cursors.DictCursor
        }
    def get_connection(self):
        try:
            connection = pymysql.connect(**self.connection_config)
            return connection
        except pymysql.Error as e:
            print(f"Помилка підключення до MySQL: {e}")
            raise


def test_connection():
    connector = MySQLConnector()
    try:
        conn = connector.get_connection()
        print("Підключення до бази даних MySQL успішно встановлено!")
        conn.close()
    except Exception as e:
        print(f"Помилка підключення: {e}")

test_connection()