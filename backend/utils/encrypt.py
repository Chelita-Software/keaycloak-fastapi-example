import base64
from cryptography.fernet import Fernet

from backend.settings.base import SECRET_KEY


class CookieEncrypter:
    secret_key = SECRET_KEY
    cipher_suite = Fernet(base64.b64encode(secret_key.encode()))

    @classmethod
    def encrypt(cls, token):
        token_bytes = token.encode('utf-8')
        encrypted_data = cls.cipher_suite.encrypt(token_bytes)
        return encrypted_data.decode('utf-8')

    @classmethod
    def decrypt(cls, encrypted_token):
        encrypted_token_bytes = encrypted_token.encode('utf-8')
        decrypted_data = cls.cipher_suite.decrypt(encrypted_token_bytes)
        return decrypted_data.decode('utf-8')
