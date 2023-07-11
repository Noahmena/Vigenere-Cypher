ciphertext = input()
key = input()
def repeat_to_length(string_to_expand, length):
   return (string_to_expand * (int(length/len(string_to_expand))+1))[:length]
if(len(ciphertext) != len(key)):
    key = repeat_to_length(key, len(ciphertext))
plaintext = ""
offset = 0
for index, x in enumerate(ciphertext):
    if(ciphertext[index].isalpha()):
        if((ord(ciphertext[index]) - 96) > 0):
            plaintext += chr((((ord(ciphertext[index]) - 97) - (ord(key[index-offset].lower()) - 97)) % 26) + 97)

        else:
            plaintext += chr((((ord(ciphertext[index]) - 65) - (ord(key[index-offset]) - 65)) % 26) + 65)
    else:
        plaintext += ciphertext[index]
        offset += 1 # do not continue with key if ciphertext char is not a letter
print(plaintext)
