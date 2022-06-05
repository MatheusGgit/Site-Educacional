from peewee import MySQLDatabase

class Connection:
    def connect(self):
        return MySQLDatabase('lmg_arts_db', user='root', password='fer@1988', host='127.0.0.1', port=3306)
