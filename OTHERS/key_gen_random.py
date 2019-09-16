import random

key_strength = 10
key_length = random.randint(6,12)

with open("randKey.txt","w") as key_file:
    for i in range(key_length):
        key_file.write(str(random.randint(1, key_strength-1))+" ")
