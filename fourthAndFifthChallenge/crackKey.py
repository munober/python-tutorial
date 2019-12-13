import hashlib
import time
import datetime

with open("../firstChallenge/outRocket.txt","r+") as output:
    value1 = output.readlines()[0]
    output.close()
with open("../secondChallenge/outInsertion.txt","r+") as output:
    value2 = output.readlines()[0]
    output.close()
with open("../thirdChallenge/outAnagram.txt","r+") as output:
    value3 = output.readlines()[0]
    output.close()

hashedWord1 = hashlib.sha256(value1.encode('utf-8')).hexdigest()
hashedWord2 = hashlib.sha256(value2.encode('utf-8')).hexdigest()
hashedWord3 = hashlib.sha256(value3.encode('utf-8')).hexdigest()

if (hashedWord1 == '5d954c286c5cde7418620285e3a4f539fa85cd62b00e7b6dabddd8d9e712d8f2'):
    print("Rocketship fuel problem is correct!")
else:
    print("Rocketship fuel problem still needs some work!")
if (hashedWord2 == 'e50b4c93d0d782f1934292eddb233007d7128fad3b2d6adec3663fc144541a26'):
    print("Insertion sort problem is correct!")
else:
    print("nsertion sort problem still needs some work!")
if (hashedWord3 == 'f5abf647acb8e5442a63b16e083ba4ffddb1403e51b33fc4c67f5c65967ae1fd'):
    print("Anagram problem is correct!")
else:
    print("Anagram problem still needs some work!")