from hashlib import *
from .connection.connector import Connection


class Authentication:
    def __init__(self):
        self.__db = Connection().connect()

    def login(self, email: str, password: str) -> bool:
        pass_hash = self.get_password_hash(password)

        query = self.__db.execute_sql(
            f"SELECT email, senha FROM paginas_usuarios WHERE email = '{email}' AND senha = '{pass_hash}';"
        )

        item = query.fetchone()

        if item is None:
            return False
        else:
            return True

    # CRIPTOGRAFA SENHA
    def get_password_hash(self, password: str) -> str:
        salt = b'1'  # Get the salt you stored for *this* user

        return str(pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt,
            100000
        ).hex())
