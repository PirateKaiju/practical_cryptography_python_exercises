import os
import string

msg = bytes(string.ascii_lowercase[:16], 'utf-8')
rdm_msg = os.urandom(16)

print("Orig.: " + "".join(string.ascii_lowercase[:16])) 

output = []

for textbyte, rdm_textbyte in zip(msg, rdm_msg):
    output.append(textbyte ^ rdm_textbyte)

readable_xor_result = "".join(map(chr, output))
print(readable_xor_result)

unxored_output = []

for textoutput, rdm_textbyte in zip(output, rdm_msg):
    unxored_output.append(textoutput ^ rdm_textbyte)

readable_result = "".join(map(chr, unxored_output))
print(readable_result)