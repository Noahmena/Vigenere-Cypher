plaintext = input()
key = input()
def repeat_to_length(string_to_expand, length):
   return (string_to_expand * (int(length/len(string_to_expand))+1))[:length]
if(len(plaintext) != len(key)):
    key = repeat_to_length(key, len(plaintext))
ciphertext = ""
offset = 0
for index, x in enumerate(plaintext):
    if(plaintext[index].isalpha()):
        if((ord(plaintext[index]) - 96) > 0):
            ciphertext += chr((((ord(plaintext[index]) - 97) + (ord(key[index-offset].lower()) - 97)) % 26) + 97)
        else:
            ciphertext += chr((((ord(plaintext[index]) - 65) + (ord(key[index-offset]) - 65)) % 26) + 65)
    else:
        ciphertext += plaintext[index]
        offset += 1 # do not continue with key if plaintext char is not a letter
print(ciphertext)
