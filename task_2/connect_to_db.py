import configparser

from mongoengine import connect

config = configparser.ConfigParser()
config.read('config.ini')

user = config.get('DB', 'user')
password = config.get('DB', 'pass')
db_name = config.get('DB', 'db_name')
domain = config.get('DB', 'domain')
app_name = config.get('DB', 'app_name')


def connect_to_db(drop: bool):
    db = connect(
        host=f'mongodb+srv://{user}:{password}@{domain}/{db_name}?retryWrites=true&w=majority&appName={app_name}',
        ssl=True
    )

    if drop:
        db.drop_database(db_name)
