import hashlib


def encrypt_password(pwd):
    sha = hashlib.sha256()
    sha.update(pwd.encode('utf8'))
    return sha.hexdigest()
