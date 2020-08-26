from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


import os
import string
from copy import deepcopy

key = os.urandom(16)

vi =  bytes('xxxxxxxxxxxxxxxx', 'utf-8')

print('VI: ', vi)


class HandmadeCounter():
    def __init__(self):
        aesCipher = Cipher(
            algorithms.AES(key),
            modes.ECB(),
            backend=default_backend()
        )


        self.aesEncriptor = aesCipher.encryptor()
        self.aesDecriptor = aesCipher.decryptor()

    def encript(self):
        message_blocks = [bytes('a'*16, 'utf-8'), bytes('b'*16, 'utf-8'), bytes('c'*16, 'utf-8')]

        counter = 0

        key_s = []

        while(counter < len(message_blocks) + 1):
            
            bytecounter = bytes(str(counter), 'utf-8').zfill(8)
            #print((bytecounter))
            #print(vi[0:8] + bytecounter)

            key_s.append(vi[0:8] + bytecounter)

            counter+=1

        encripted_keys = []

        for key in key_s:
            encripted_keys.append(self.aesEncriptor.update(key))

        print(encripted_keys)

        output = []

        for block, key in zip(message_blocks, encripted_keys):
            pre_output = []
            for byte_message, byte_key in zip(block, key):
                #print(byte_key, byte_message)
                pre_output.append(byte_message ^ byte_key)

            output.append(pre_output[:])

        print(output)
        return output

    def decript(self, ciphered_blocks):

        counter = 0

        key_s = []

        while(counter < len(ciphered_blocks) + 1):
            
            bytecounter = bytes(str(counter), 'utf-8').zfill(8)
            #print((bytecounter))
            #print(vi[0:8] + bytecounter)

            key_s.append(vi[0:8] + bytecounter)

            counter+=1

        encripted_keys = []

        for key in key_s:
            encripted_keys.append(self.aesEncriptor.update(key))

        deciphered_message = []
        
        for block, key in zip(ciphered_blocks, encripted_keys):
            dec_block = []
            for byte_cmessage, byte_key in zip(block, key):
                dec_block.append(byte_cmessage ^ byte_key)
            
            deciphered_message.append(dec_block[:])

        print(deciphered_message)
        
        return deciphered_message



#HandmadeCounter().encript()
h1 = HandmadeCounter()
h1.decript(h1.encript()) #TEST ONLY