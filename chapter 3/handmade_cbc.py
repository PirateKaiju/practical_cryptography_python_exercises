from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

import os
import string
from copy import deepcopy

key = os.urandom(16)

vi = os.urandom(16)

aesCipher = Cipher(
    algorithms.AES(key),
    modes.ECB(),
    backend=default_backend()
)


aesEncriptor = aesCipher.encryptor()
aesDecriptor = aesCipher.decryptor()

class HandmadeCBC(object):
    def __init__(self):
        aesCipher = Cipher(
            algorithms.AES(key),
            modes.ECB(),
            backend=default_backend()
        )


        self.aesEncriptor = aesCipher.encryptor()
        self.aesDecriptor = aesCipher.decryptor()

    def encript(self):
        messages = [bytes('a'*16, 'utf-8'), bytes('b'*16, 'utf-8'), bytes('c'*16, 'utf-8'), bytes('d'*16, 'utf-8')]

        pre_output = []

        for bit_vi, bit_msg in zip(vi, messages[0]):
            pre_output.append(bit_vi ^ bit_msg)

        xored_messages = [deepcopy(pre_output)]

        print(messages)
        pre_output = []

        for message in messages[1:]:
            for bit_vi, bit_msg in zip(xored_messages[len(xored_messages) - 1], message):
                pre_output.append(bit_vi ^ bit_msg)
            xored_messages.append(deepcopy(pre_output))
            pre_output = []
        
        print(xored_messages)


        #UNXOR

        for message in xored_messages:
            print("".join(map(chr, message)))

        unxored_messages = []

        pre_output = []

        i = len(xored_messages) - 2

        while(i >= 0):

            for bit_xored, bit_msg in zip(xored_messages[i], xored_messages[i + 1]):
                pre_output.append(bit_xored ^ bit_msg)
            
            unxored_messages.append(deepcopy(pre_output))
            
            pre_output = []
            i-=1

        #print(unxored_messages)


    def decript(self):
        pass

hcbc = HandmadeCBC()
hcbc.encript()