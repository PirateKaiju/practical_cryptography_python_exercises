import hashlib

with open("test.txt", "rb") as f:
    #print(f.read())
    md5hasher = hashlib.md5()

    #print(hashlib.md5(f.read()).hexdigest()) #TESTING PURPOSES
    
    for line in f:
        md5hasher.update(line)
    
    print(md5hasher.hexdigest())