######### approach #########
### FIND KEY LENGTH ###
# ...
### CRACK KEYS ###
# Following steps for each possible key length
# 1. For each position: try all keys, create a list of keys from most to least probably depending on freq. analysis
# 2. Cut each list to the first n elements
# 3. Brute force through the filtered keys, if recognizable vocabs > 20% -> successful

#!/usr/local/bin/python3
import collections
import time
import sys
import itertools
import string
import argparse
from main import decipher_137enhanced, decipher_key_137enhanced

################# FIND KEY LENGTH ###################
def merge_list(list):
    res = []
    for sublist in list:
        res += sublist
    return res

def find_factors(key_len):
    """ returns lengths of possibly repeated keys """

    factors = set()
    for i in range(2, key_len+1):
        if key_len % i == 0:
            factors.add(i)
    return sorted(factors)

def possible_spacings(str):
    seq_to_spacings = {}
    for seq_len in range(3, 6):     # find spacings for patterns of 3-5 characters
        for seq_start in range(len(str) - seq_len):
            seq = str[seq_start:seq_start + seq_len]
            for i in range(seq_start + seq_len, len(str) - seq_len):
                if str[i:i + seq_len] == seq:
                    if seq not in seq_to_spacings:
                        seq_to_spacings[seq] = []
                    seq_to_spacings[seq].append(i - seq_start)
    spacings = []   # list of all spacings
    for spacing_list in seq_to_spacings.values():
        spacings += [find_factors(spacing) for spacing in spacing_list] # spacings + list of factor lists
    spacings = merge_list(spacings) # spacings = list of all factors (possible key lengths)
    ranged_spacings = []
    for spacing in sorted(spacings, key=lambda x: spacings.count(x), reverse=True):
        if spacing not in ranged_spacings:
            ranged_spacings.append(spacing)
    return ranged_spacings  # unique spacings sorted from most to least common


####################################################


def get_freq_ltrs(str):
    """ returns a string of letters arranged from the most frequent to the least, used on a try-n-cracked msg """

    ltr_to_freq = collections.defaultdict(int)
    for ltr in str:
        ltr_to_freq[ltr.upper()] += 1
    return "".join([pair[0] for pair in sorted(ltr_to_freq.items(), key=lambda x:x[1], reverse=True) if pair[0].isalpha()])

def ranged_keys(segmented_str, key_strength):
    key_to_accScore = dict()
    etaoin = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
    for current_key in range(key_strength):
        acc_score = 0
        deciphered = decipher_137enhanced(segmented_str, current_key)
        freqstring = get_freq_ltrs(deciphered)
        for c in freqstring[:6]:
            if c in etaoin[:6]:
                acc_score += 1
        for c in freqstring[-6:]:
            if c in etaoin[-6:]:
                acc_score += 1
        key_to_accScore[current_key] = acc_score
    # returns a list of keys from most to least suitable
    return [tup[0] for tup in sorted(key_to_accScore.items(), key=lambda x: x[1], reverse=True)]

def cut_to_n_most_common(ranged_lists, n=3):
    return [list[:n] for list in ranged_lists]
    # [][:n] for each key, return all [] in a list

def get_all_possible_keys(cut_lists):
    """ returns a list of all possbible keys from lists of n most suitable keys for one position """

    return list(itertools.product(*cut_lists))

def brute_force(msg, key, lexicon):
    """ str = encrypted msg, pos_keys = list of possible keys, lexicon = string read from a dictionary file """

    deciphered_txt = decipher_key_137enhanced(msg, key)
    deciphered_words = {word.strip(string.punctuation).upper() for word in deciphered_txt.split()}
    words_in_lexicon = 0
    for word in deciphered_words:
        if word in lexicon:
            words_in_lexicon += 1
    if words_in_lexicon/len(deciphered_words) >= 0.2:
        return True
    return False

################# BRUTE FORCE ALL POS SPACINGS ###################
def space_force(msg, spacing_list, lexicon):
    searching = True
    for key_length in spacing_list:
        if searching:
            print("\nTrying key length " + str(key_length))
            ranged_lists = []
            for key_pos in range(key_length):
                sengmented_str = enciphered[key_pos::key_length]
                ranged_lists.append(ranged_keys(sengmented_str, key_strength))
            cut_list = cut_to_n_most_common(ranged_lists)   # auto 3 most common
            all_keys = get_all_possible_keys(cut_list)
            key_num = 1
            for key in all_keys:
                sys.stdout.write("\rTrying key#"+str(key_num))
                sys.stdout.flush()
                if brute_force(enciphered, key, lexicon):
                    print("\nkey#%d successful: %s" % (key_num, key))
                    searching = False
                    break
                key_num += 1

##################################################################


parser = argparse.ArgumentParser(description="FREQENCY ANALYSIS FOR VIGENÈRE CIPHER")
parser.add_argument("-f", "--file", help="Specify encrypted file.", required=True)
args = parser.parse_args(sys.argv[1:])

start_time = time.time()


with open(args.file) as file:
    enciphered = file.read()
with open("dictionary.txt") as dictionary:
    en_words = dictionary.read().split()

key_strength = 20
# key_lengths = possible_spacings(enciphered)     # using enciphered, investigate all possible lengths

space_force(enciphered, possible_spacings(enciphered), en_words)

end_time = time.time()
print("\nFinished in "+str(round(end_time-start_time, 2))+" second(s).")

# ranged_lists = []
# for key_pos in range(key_length):
#     sengmented_str = enciphered[key_pos::key_length]
#     ranged_lists.append(ranged_keys(sengmented_str, key_strength))
# cut_list = cut_to_n_most_common(ranged_lists)   # auto 3 most common
# all_keys = get_all_possible_keys(cut_list)

# key_num = 1
# for key in all_keys:
#     sys.stdout.write("\rTrying key#"+str(key_num))
#     sys.stdout.flush()
#     if brute_force(enciphered, key, en_words):
#         print("\nkey#%d successful: %s" % (key_num, key))
#         break

#         # USER FEEDBACK REQUIRED -- COMMENT OUT "BREAK" ABOVE
#         # print("\nDecrypted msg: " + decipher_key(enciphered, key), end="\r")
#         # action = input("ENTER = continue trying, STH ELSE + ENTER = cancel --")
#         # if action == "":
#         #     continue
#         # else:
#         #     break

#     key_num += 1



#################### deprecated ###################
# def crack_key_en(segmented_str, key_strength):
#     """ returns the most possible key for one position of the key, knowledge of key length required """

#     key_to_accScore = dict()
#     etaoin = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
#     for current_key in range(key_strength):   # strength 32 -> encrypt possibility 0-31
#         acc_score = 0
#         deciphered = decipher(segmented_str, current_key)
#         freqstring = get_freq_ltrs(deciphered)
#         for c in freqstring[:6]:
#             if c in etaoin[:6]:
#                 acc_score += 1
#         for c in freqstring[-6:]:
#             if c in etaoin[-6:]:
#                 acc_score += 1
#         key_to_accScore[current_key] = acc_score
#     # ranged_keys = sorted(key_to_accScore.items(), key=lambda x: x[1], reverse=True)
#     return sorted(key_to_accScore.items(), key=lambda x:x[1], reverse=True)[0][0]

################## ONLY BEST KEY ###################
# keys = []
# for key_pos in range(key_length):
#     sengmented_str = enciphered[key_pos::key_length]
#     sys.stdout.write("\rCracking key at position: "+str(key_pos+1))
#     sys.stdout.flush()
#     cracked_key = crack_key_en(sengmented_str, key_strength)
#     print("\nBest key at position %d: %d" %(key_pos+1, cracked_key))
#     keys.append(cracked_key)
# print("\nBest keys: ", key)
####################################################
