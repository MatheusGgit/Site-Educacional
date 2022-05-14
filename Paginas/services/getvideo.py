from .connection.connector import Connection

class cursoVideos:
    def __init__(self):
        self.__db = Connection().connect()

    def video_get(self, id_curso) -> bool:

        query = self.__db.execute_sql(
            f"SELECT id FROM paginas_video WHERE cursoID_id = '{id_curso}';"
        )

        item = query.fetchall()
        if len(item) != 0:  # Verifica se o retorno contém alguma linha
            return item
        else:
            return False
