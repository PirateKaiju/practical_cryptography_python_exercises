from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

import os
import string
from copy import deepcopy

key = os.urandom(16)

# vi = os.urandom(16)
#FOR TESTING PURPOSES, ENSURE THIS VI VALUE IS MORE "CONTROLLED"
vi =  bytes('xxxxxxxxxxxxxxxx', 'utf-8')

print(vi)

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
        #TODO: PASS MESSAGE AND HANDLE BYTE FILLING
        messages = [bytes('a'*16, 'utf-8'), bytes('b'*16, 'utf-8'), bytes('c'*16, 'utf-8'), bytes('d'*16, 'utf-8')]

        

        pre_output = []

        #FIRST BLOCK OF THE MESSAGE USES THE VI KEY
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
        
        print("CORE XOR OUTPUT")
        print(xored_messages)
        
        #PRINT
        for message in xored_messages:
            print(len(message))
            print("".join(map(chr, message)))

        full_message = ""

        for message in xored_messages:
            full_message += "".join(map(chr, message))

        
        #print(bytes("".join(map(chr, message)), 'utf-8'))
        #print(len(full_message))

        #print(bytes(full_message, 'utf-8'))

        print("Full Message")
        print(full_message)

        bfull_message = bytes(full_message, 'utf-8') 

        bfull_message += b'\x00' * (16 - (16 % len(bfull_message))) #LAZY MAN'S PADDING

        print("Full Message in Binary: ")
        print( bfull_message)
        #return
        
        ciphered_full_message = self.aesEncriptor.update(bfull_message)

        print("Full Cyphered Message: ")
        print( ciphered_full_message)

        '''deciphered_full_message = self.aesDecriptor.update(ciphered_full_message)

        print(deciphered_full_message)

        print(deciphered_full_message.decode('utf-8'))'''

        return ciphered_full_message

        ###UNXOR

        '''unxored_messages = []

        pre_output = []

        i = len(xored_messages) - 2

        while(i >= 0):

            for bit_xored, bit_msg in zip(xored_messages[i], xored_messages[i + 1]):
                pre_output.append(bit_xored ^ bit_msg)
            
            unxored_messages.append(deepcopy(pre_output))
            
            pre_output = []
            i-=1

        for bit_vi, bit_msg in zip(vi, xored_messages[0]):
            pre_output.append(bit_vi ^ bit_msg)

        unxored_messages.append(deepcopy(pre_output))
        print(unxored_messages)

        for message in unxored_messages:
            print("".join(map(chr, message)))'''


    def decript(self, ciphered_full_message):

        print("Full Cyphered Message: ")
        print( ciphered_full_message)


        deciphered_full_message = (self.aesDecriptor.update(ciphered_full_message)).decode()

        #print(len(deciphered_full_message))

        print("Full deciphered message")
        print(deciphered_full_message)
        
        #The decode is just for easing the splitting
        xored_messages = [deciphered_full_message[x:x + 16] for x in range(0, len(deciphered_full_message), 16)]


        '''print("XOR-ed Messages")
        print(xored_messages)

        print(len(xored_messages))'''

        
        print("XOR-ed Messages")
        for message in xored_messages:
            print(len(message))
            print(message)
        #DECODE HAVING PROBLEMS WITH LOSS
        #return
        
        xored_messages = [str.encode(x) for x in xored_messages]

        print(xored_messages)


        unxored_messages = []

        pre_output = []

        i = len(xored_messages) - 2

        while(i >= 0):

            for bit_xored, bit_msg in zip(xored_messages[i], xored_messages[i + 1]):
                pre_output.append(bit_xored ^ bit_msg)
            
            unxored_messages.append(deepcopy(pre_output))
            
            pre_output = []
            i-=1

        for bit_vi, bit_msg in zip(vi, xored_messages[0]):
            pre_output.append(bit_vi ^ bit_msg)

        unxored_messages.append(deepcopy(pre_output))
        print("Unxored")
        print(unxored_messages)

        for message in unxored_messages:
            print("".join(map(chr, message)))
        pass
        

hcbc = HandmadeCBC()

result = hcbc.encript()
hcbc.decript(result)