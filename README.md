# pastegram-py

A set of simple functions to upload and fetch pastes on [paste.uploadgram.me](https://paste.uploadgram.me/).

## API Documentation

### Methods

#### `upload_paste(contents: bytes, filename: str) -> UploadedPaste`:

Uploads a paste.

| argument | required | default |
| -------- | -------- | ------- |
| contents | yes      |         |
| filename | no       | paste   |

Returns: the `UploadedPaste`

#### `fetch_paste(url: str) -> str`

Fetches the paste and returns the contents as string.

| argument | required | default |
| -------- | -------- | ------- |
| url      | yes      |         |

Returns: The paste's contents as string

### Types

#### `UploadedPaste`

An uploaded paste

##### Fields

| field      | type  | description                                          |
| ---------- | ----- | ---------------------------------------------------- |
| token      | str   | An unique token that can be used to delete the paste |
| downloadId | str   | The paste's download id                              |
| key        | bytes | The paste's decryption key as bytes                  |

##### Methods

`UploadedPaste.get_url() -> str`

Gets the paste's shareable url

### Errors

#### `ParseError`

Raised when an error occurs while parsing. May be thrown by `fetch_paste()`

#### `APIError`

Raised when an error occurs while fetching/parsing an API reponse. May be thrown by `upload_paste()`

### Examples

Upload a paste and fetch it back

```py
from pastegram import upload_paste, fetch_paste, UploadedPaste

def main():
    print('uploading paste...')
    paste: UploadedPaste = upload_paste(b'hello')
    print(paste.token)
    print(paste.get_url())

    print('re-downloading paste...')
    contents: str = fetch_paste(paste.get_url())
    print(contents)

if __name__ == '__main__':
    main()
```
