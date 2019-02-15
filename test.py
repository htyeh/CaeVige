#!/usr/local/bin/python3


la_alphabet = "abcdefghijklmnopqrstuvwxyzäöüßABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ !\"$%&'()*+,-./:;<=>?@[\]_"

def encipher(string, n, alphabet):
    
    res = ""
    for ltr in string:
        if ltr in alphabet:
            encipher_index = alphabet.find(ltr)+n
            if encipher_index >= len(alphabet):
                res += alphabet[encipher_index-len(alphabet)]
            else:
                res += alphabet[encipher_index]
        else:
            res += ltr
    return res


def sublist(list, n):
    for i in range(0, len(list), n):
        yield list[i:i+n]


def encipher_key(string, key, alphabet):
    if len(string) <= len(key):
        return "".join([enciphered for enciphered in map(encipher, string, key, alphabet)])
        # return "".join([encipher(char, n) for char in string for n in key])
    else:
        str_segs = sublist(string, len(key))
        res = ""
        for string in str_segs:
            res += "".join([enciphered for enciphered in map(encipher, string, key, alphabet)])
            # res += "".join([encipher(char, n) for char in string for n in key])
        return res


sent = "this morning"
print(encipher_key(sent, [1,5,1,7,9,8,4,2,3,6,1,8,9,4,6,3,6,2,7,0,7,1,1,2,6,3,7,9,3], la_alphabet))
