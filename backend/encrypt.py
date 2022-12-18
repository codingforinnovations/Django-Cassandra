import pathlib
from decouple import config

from cryptography.fernet import Fernet

ENCRYPTION_KEY = config('ENCRYPTION_KEY', cast=str)

def generate_key():
    return Fernet.generate_key().decode("UTF-8")


def encrypt_dir(input_dir, output_dir):
    key = ENCRYPTION_KEY
    if not key:
        raise Exception("No encryption key found")

    fer = Fernet(key)
    input_dir = pathlib.Path(input_dir)
    output_dir = pathlib.Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    for path in input_dir.glob('*'):
        _path_bytes = path.read_bytes()
        data = fer.encrypt(_path_bytes)
        rel_path = path.relative_to(input_dir)
        des_path = output_dir / rel_path
        des_path.write_bytes(data)


def decrypt_dir(input_dir, output_dir):
    key = ENCRYPTION_KEY
    if not key:
        raise Exception("No encryption key found")

    fer = Fernet(key)
    input_dir = pathlib.Path(input_dir)
    output_dir = pathlib.Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    for path in input_dir.glob('*'):
        _path_bytes = path.read_bytes()
        data = fer.decrypt(_path_bytes)
        rel_path = path.relative_to(input_dir)
        des_path = output_dir / rel_path
        des_path.write_bytes(data)