# By default, 20% of the words must exist in the dictionary file, and
# 85% of all the characters in the message must be letters or spaces
from main import decipher_key
import sys
import time
import itertools
import string
import argparse

parser = argparse.ArgumentParser(description="FORCE CRACK ENCRYPTION KEY")
parser.add_argument("-f", "--file", help="Specify encrypted file.", required=True)
args = parser.parse_args(sys.argv[1:])

def try_key(str,key,lexicon):
    deciphered_txt = decipher_key(str,key)
    deciphered_words = {word.strip(string.punctuation).upper() for word in deciphered_txt.split()}
    words_in_lexicon = 0
    for word in deciphered_words:
        if word in lexicon:
            words_in_lexicon += 1
    if words_in_lexicon/len(deciphered_words) >= 0.2:
        return True
    return False

key_strength = int(input("Enter single key strength: "))
key_bit = int(input("Enter number of bits: "))

start_time = time.time()

key_range = [i for i in range(key_strength)]
key_bit_range = []
for i in range(key_bit):
    key_bit_range.append(key_range)
all_keys = list(itertools.product(*key_bit_range))

with open("dictionary.txt") as dictionary:
    en_words = dictionary.read().split()

with open(args.file) as enciphered:
    msg = enciphered.read()

key_num = 1
for key in all_keys:
    sys.stdout.write("\rTrying key#"+str(key_num))
    sys.stdout.flush()
    if try_key(msg,key,en_words):
        print("\nkey#%d successful: %s" %(key_num,key))
        break
    key_num += 1

end_time = time.time()
print("\nFinished in "+str(round(end_time-start_time, 2))+" second(s).")
