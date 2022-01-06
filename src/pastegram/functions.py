import requests;
from .classes import UploadedPaste
from .constants import *
from .utils import decrypt_paste, encrypt_paste, parse_paste_url
from .errors import APIError

def upload_paste(contents: bytes, filename: str = 'paste') -> UploadedPaste:
    """Uploads (and encrypts) a paste on paste.uploadgram.me"""
    key, encrypted_message = encrypt_paste(contents)
    response = requests.put(API_ENDPOINT + 'upload', encrypted_message, headers={
        'content-type': 'application/octet-stream',
        'upload-filename': filename,
    })
    if response.status_code != 201:
        raise APIError('Unexpected status_code')
    res_data = response.json()
    if not res_data['ok']:
        raise APIError('Request failed with message ' + res_data['message'])
    url: str = res_data['url']
    if not url.startswith(DOWNLOAD_ENDPOINT):
        raise APIError('Invalid URL in response')
    downloadId = url[len(DOWNLOAD_ENDPOINT):]
    return UploadedPaste(res_data['delete'], downloadId, key)

def fetch_paste(url: str) -> str:
    """Fetches (and decrypts) a paste from paste.uploadgram.me"""
    raw_url, key = parse_paste_url(url)
    response = requests.get(raw_url)
    if response.status_code != 200:
        raise APIError('Unexpected status_code')
    return decrypt_paste(response.content, key)
