from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

import os

key = os.urandom(16)

aesCipher = Cipher(
    algorithms.AES(key),
    modes.ECB(),
    backend=default_backend()
)


aesEncriptor = aesCipher.encryptor()
aesDecriptor = aesCipher.decryptor()

encripted_result = aesEncriptor.update(b'secret message secret message secret message secret message')

print(encripted_result)
print(aesDecriptor.update(encripted_result))