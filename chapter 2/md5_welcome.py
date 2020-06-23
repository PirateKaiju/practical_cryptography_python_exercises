import hashlib

print(hashlib.md5(b'alice').hexdigest())
print(hashlib.md5(b'a').hexdigest())
print(hashlib.md5(b'a'*10).hexdigest())