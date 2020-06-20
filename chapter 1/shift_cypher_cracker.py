
from shift_cypher import cypher, alphabet

#Assuming the attacker know only the cypher function

def cracker(text):
    for i in range(len(alphabet)):
        current_result = cypher(text, i)

        current_shift = (len(alphabet) - i)

        print(current_result)

        usr_response = input("Continue execution (Y/N)?")

        if usr_response == "N":
            return current_result, current_shift
        

print(cypher("Hello World", 5))

cracker(cypher("Hello World", 24))