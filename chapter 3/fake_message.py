from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

import os

def fill_to_multiple(text):
    if (len(text) % 16) != 0:
        text += b" " * (16 - (len(text) % 16))
    
    return text

key = os.urandom(16)

message1 = b"Message Header \n Message Body \n Location of meeting"

message2 = b"Message Header \n Another Message Body \n Another Location of meeting"

message1 = fill_to_multiple(message1)
message2 = fill_to_multiple(message2)

aesCipher = Cipher(
    algorithms.AES(key),
    modes.ECB(),
    backend=default_backend()
)

aesEncriptor = aesCipher.encryptor()
aesDecriptor = aesCipher.decryptor()

#print(len((message1)))

encripted_message1 = aesEncriptor.update(message1)
encripted_message2 = aesEncriptor.update(message2)

#print(encripted_message1)
#print(aesDecriptor.update(encripted_message1))

#print((encripted_message1))

fake_message = encripted_message1[:32] + encripted_message2[32:]

#print(fake_message)
print(aesDecriptor.update(fake_message))