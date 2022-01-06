from pastegram.functions import upload_paste, fetch_paste
print('uploading paste...')
paste = upload_paste(b'hello')
print(paste.token)
print(paste.get_url())
print(f'{paste.key=}' )

print('re-downloading paste...')
print(fetch_paste(paste.get_url()))