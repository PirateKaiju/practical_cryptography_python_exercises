#USING RAW LOGICS
def xor(a, b):
    return ((a or b) and (not (a and b))) 

print(xor(False, False))
print(xor(True, False))
print(xor(False, True))
print(xor(True, True))

#USING THE XOR OPERATOR
print(True ^ True)