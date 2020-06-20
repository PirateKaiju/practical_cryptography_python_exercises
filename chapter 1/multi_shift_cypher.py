import string
import random

alphabet = list(string.ascii_lowercase)

aux_alphabet_indexes = [x for x in range(len(alphabet))]

'''print(aux_alphabet_indexes)

random.shuffle(aux_alphabet_indexes)

print(aux_alphabet_indexes)'''

def cypher(text):

    alphabet_indexes = random.sample(aux_alphabet_indexes, len(aux_alphabet_indexes))

    cyphertext = ""

    for char in text:
        if char == " ":
            cyphertext += char
        else:
            current_index = alphabet.index(char)
            cyphertext += alphabet[alphabet_indexes[current_index]]
    
    return cyphertext, alphabet_indexes

def decypher(text, alphabet_indexes):

    decyphertext = ""

    for char in text:

        if char == " ":
            decyphertext += char
        else:
            
            current_cypherchar_index = alphabet.index(char)
            current_corresp_char_index = alphabet_indexes.index(current_cypherchar_index)

            decyphertext += alphabet[current_corresp_char_index]
    
    return decyphertext, alphabet_indexes

res, alph = cypher("test of cypher")

print(res)

dec_res, alph = decypher(res, alph)

print (dec_res)