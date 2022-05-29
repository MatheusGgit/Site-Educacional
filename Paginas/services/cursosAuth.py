from .connection.connector import Connection

class userCursos:
    def __init__(self):
        self.__db = Connection().connect()

    def email_get(self, email: str) -> bool:

        query = self.__db.execute_sql(
            f"SELECT id FROM lmg_arts_db.paginas_usuarios WHERE email = '{email}';"
        )

        item = query.fetchone()
        if len(item) != 0:  # Verifica se o retorno contém alguma linha
            return item[0]
        else:
            return False
