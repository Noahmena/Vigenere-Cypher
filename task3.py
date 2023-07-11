import math
from collections import Counter
from string import ascii_lowercase, ascii_uppercase
ciphertext = input()
keyLen = int(input())
uppers = ascii_uppercase
lowers = ascii_lowercase
ciphDict = {}
for x in range(1, keyLen+1):
    ciphDict["key{0}".format(x)] = ''
if (keyLen < len(ciphertext)):
    y = 1
    for x in ciphertext:
        ciphDict["key{0}".format(y)] += x
        if x in lowers or x in uppers:
            y += 1
        if (y > keyLen):
            y = 1


LETTER_FREQUENCY = {'e': .127, 't': .0906, 'a': .0817, 'o': .0751, 'i': .0697, 'n': .0675, 's': .0633, 'h': .0609,
                    'r': .0599, 'd': .0425, 'l': .0403, 'c': .0278, 'u': .0276, 'm': .0241, 'w': .0236, 'f': .0223,
                    'g': .0202, 'y': .0197, 'p': .0193, 'b': .0129, 'v': .0098, 'k': .0077, 'j': .0015, 'x': .0015,
                    'q': .0010, 'z': .0007}

def findScore(plaintext: str) -> float:
    plaintext = plaintext.lower()
    counter = Counter(plaintext)
    score = 0
    for x in lowers:
        if x in lowers:
            letterScore = LETTER_FREQUENCY.get(x, 0) * len(plaintext)
            score += ((counter.get(x, 0) - letterScore) ** 2)/letterScore
    return score

plainDict = {}
for x in range(1, keyLen+1):
    plainDict["key{0}".format(x)] = ''

keyDict = {}
for x in range(1, keyLen+1):
    keyDict["key{0}".format(x)] = ''

for key, value in ciphDict.items():
    score = math.inf
    scoreDict = {}
    for z in range(1, 26):
        scoreDict["char{0}".format(z)] = 0

    for x in range(0, 25):
        plaintext = ''
        for y in value:
            if y in uppers:
                num = uppers.find(y)
                num = num - x
                if num < 0:
                    num = num + len(uppers)
                plaintext = plaintext + uppers[num]
            elif y in lowers:
                num = lowers.find(y)
                num = num - x
                if num < 0:
                    num = num + len(lowers)
                plaintext = plaintext + lowers[num]
            else:
                plaintext = plaintext + y
        temp = findScore(plaintext)
        scoreDict["char{0}".format(x)] = temp

        if temp < score:
            score = temp
            plainDict[key] = plaintext
            keyDict[key] = chr(x+97)
key = ''
for keys in keyDict:
    key += keyDict[keys]
key = key.upper()
keyPrint = key


def repeat_to_length(string_to_expand, length):  #https://stackoverflow.com/questions/53067975/how-to-repeat-a-string-in-python-to-a-certain-length
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

print(keyPrint)


