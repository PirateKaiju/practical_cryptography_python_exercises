
def permutations(alphabet, max_length):

    words = []

    #BOOTSTRAP
    for letter in alphabet:
        words.append(letter)
        
    for word in words:
        #Iterates over itself

        if len(word) == max_length:
            return words
        
        for letter in alphabet:
            words.append(word + letter)

    return words

#print(permutations("abcte", 7))

'''
a
b
c
aa
ab
ac
ba
bc
bc
ca
cb
cd
aaa
...
'''
