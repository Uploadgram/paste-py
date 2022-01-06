from base64 import urlsafe_b64encode
from .constants import PASTEGRAM_ENDPOINT

class UploadedPaste:
    token: str
    downloadId: str
    key: bytes

    def __init__(
        self,
        token: str,
        downloadId: str,
        key: bytes,
    ):
        self.token = token
        self.downloadId = downloadId
        self.key = key

    def __str__(self):
        return f'UploadedPaste({self.token}, {self.downloadId}, {self.key})'

    def get_url(self) -> str:
        key_encoded = urlsafe_b64encode(self.key).decode().replace('=', '')
        return f'{PASTEGRAM_ENDPOINT}{self.downloadId}#{key_encoded}'