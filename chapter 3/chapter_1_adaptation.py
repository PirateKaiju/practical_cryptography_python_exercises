from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

import os

key = os.urandom(16)

def fill_bytes(text):
    
    
    text += " " * (16 - len(text))
    
    return text

#TODO: MAKE AN "UNFILL BYTES"

def encript(text, key):
    
    aesCipher = Cipher(
        algorithms.AES(key),
        modes.ECB(),
        backend=default_backend()
    )

    if len(text) < 16:
        text = fill_bytes(text)

    byte_text = bytes(text, 'utf-8')

    #print(byte_text)
    #print(len(byte_text))

    encripted_text = aesCipher.encryptor().update(byte_text)

    return encripted_text

def decript(encripted_text, key):

    aesCipher = Cipher(
        algorithms.AES(key),
        modes.ECB(),
        backend=default_backend()
    )

    #byte_text = bytes(encripted_text, 'utf-8')

    decripted_text = aesCipher.decryptor().update(encripted_text)

    return decripted_text

#TODO: HANDLE ENCONDING BETTER

encripted_text = encript("Test text  ", key)

print(encripted_text)

decripted_text = decript(encripted_text, key)

print(decripted_text)