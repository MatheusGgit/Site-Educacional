from django.test import TestCase
from peewee import MySQLDatabase

class Connection:
    def connect(self):
        return MySQLDatabase('site_educacional', user='root', password='felipe12345', host='127.0.0.1', port=3306)

__db = Connection().connect()

def video_get(id_curso):
    query = __db.execute_sql(
        f"SELECT video FROM paginas_video WHERE cursoID_id = '{id_curso}';"
    )

    item = query.fetchall()

    for i in item:
        print(f'Resultado: {item}')


video_get(id_curso=3)




