import string

alphabet = list(string.ascii_lowercase)

#print(alphabet)

def cypher(text, shift):

    text = text.lower()

    cyphertext = ""

    for char in text:
        #TODO: CONSIDER OTHER SYMBOLS, WILL BREAK ON USING PUNCTUATION
        if char == " ":
            cyphertext += char
        else:
            
            cypher_char_index = ((alphabet.index(char) + shift) % len(alphabet))

            #NON MODULUS BASED METHOD
            '''if(cypher_char_index > len(alphabet) - 1):
                cypher_char_index = cypher_char_index - len(alphabet)
            '''
            cyphertext += alphabet[cypher_char_index]

    return cyphertext

def decypher(text, shift):
    # IT WORKS
    return cypher(text, len(alphabet) - shift)




print(cypher("Hello zzabc yxvuwlll", 5))
print(decypher(cypher("Hello zzabc yxvuwlll", 5), 5))
