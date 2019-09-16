# random.randint(1,len(alphabet)-1)

import os
import random

print("What would you like to do?")
print("\t1. Overwrite key.txt (auto. 32bit)")
print("\t2. Create a new key")
choice = input(">>> ")

if choice == "1":
    with open("key.txt","w") as key:
        for i in range(0,32):
            key.write(str(random.randint(1,84))+" ")

else:
    print("creating a new key")
    new_name = input("Enter a file name: ")
    strength = int(input("Enter single key strength: "))
    num_bits = int(input("Enter # of bits: "))

    with open(new_name, "w") as key:
        for i in range(0,num_bits):
            key.write(str(random.randint(0,strength-1))+" ")
