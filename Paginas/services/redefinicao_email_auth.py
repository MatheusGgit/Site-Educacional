from hashlib import *
from .connection.connector import Connection

class Authentication_email:
    def __init__(self):
        self.__db = Connection().connect()

    def email_get(self, email: str) -> bool:

        query = self.__db.execute_sql(
            f"SELECT email FROM paginas_usuarios WHERE email = '{email}';"
        )

        item = query.fetchall()
        if len(item) != 0:  # Verifica se o retorno contém alguma linha
            return True
        else:
            return False

class Email_Redef:
    def __init__(self):
        self.__db = Connection().connect()

    def email_redef(self, password, password2, email):
        if password != password2:
            return False
        else:
            pass_hash = self.get_password_hash(password)
            query = self.__db.execute_sql(
                f"UPDATE paginas_usuarios SET senha = '{pass_hash}' WHERE email = '{email}';"
            )
            return True

    def get_password_hash(self, password: str) -> str:
        salt = b'1'  # Get the salt you stored for *this* user

        return str(pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt,
            100000
        ).hex())
