import hashlib
data = "Hello world!"
md5_hash = hashlib.md5(data.encode('utf-8')).hexdigest()
print(md5_hash)