from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from base64 import urlsafe_b64decode
from .constants import *
from .errors import ParseError


def decrypt_paste(encrypted: bytes, key: bytes) -> str:
    """Decrypts a Pastegram paste"""
    iv = encrypted[:12]
    encrypted_message = encrypted[12:-16]
    tag = encrypted[-16:]
    cipher = AES.new(key, AES.MODE_GCM, iv)
    contents = cipher.decrypt_and_verify(encrypted_message, tag)
    return contents.decode()

def encrypt_paste(contents: bytes) -> bytes:
    """Encrypts a paste to be uploaded on Pastegram"""
    key = get_random_bytes(32)
    iv = get_random_bytes(12)
    cipher = AES.new(key, AES.MODE_GCM, iv)
    ciphertext, tag = cipher.encrypt_and_digest(contents)
    return key, (iv + ciphertext + tag)

def parse_paste_url(url: str) -> (str, bytes):
    """Parses a paste url, returning respectively the raw url (dl.uploadgram.me, as string) and the key (as bytes, decoded)"""
    if not url.startswith(PASTEGRAM_ENDPOINT):
        raise ParseError('Non-valid url')
    if url.find('#') == -1:
        raise ParseError('No key in url')
    url = url[len(PASTEGRAM_ENDPOINT):]
    downloadId, encoded_key = url.split('#')
    key = urlsafe_b64decode(__pad_base64(encoded_key.encode()))
    return f'{DOWNLOAD_ENDPOINT}{downloadId}?raw', key

def __pad_base64(base64: bytes) -> bytes:
    pad_len = len(base64) % 4
    if pad_len:
        base64 += b'=' * (4 - pad_len)
    return base64