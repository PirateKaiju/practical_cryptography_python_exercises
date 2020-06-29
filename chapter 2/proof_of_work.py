import hashlib

max_attempts = 100000

leading_zeroes = 4

i = 0
while i < max_attempts:
    current_hash = hashlib.sha256(bytes(str(i), 'utf-8')).hexdigest()
    
    print(current_hash)
    #print(current_hash[:4])

    if(current_hash[:leading_zeroes] == ("0"*leading_zeroes)):
        print("Found at: " + str(i) + " - Hash: " + current_hash)
        break

    i += 1