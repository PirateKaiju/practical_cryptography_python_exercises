#DONT RUN THIS WITHOUT A CONTROLLED ENVIRONMENT

import hashlib
import string

from alphabet_permutations import permutations


'''print(bytes('a', 'utf-8'))
print((b'a'))'''

words = permutations('abcd', 3)

hashed_sample_letter = hashlib.md5(b'z').hexdigest()
print(hashed_letter)

for word in words:
    #print(word)
    if hashed_sample_letter == hashlib.md5(bytes(word, 'utf-8')).hexdigest() :
        print("Found at " + word) 
        break