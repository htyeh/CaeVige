# -*- coding: utf-8 -*-

import sys

def sublist(list, n):
    for i in range(0, len(list), n):
        yield list[i:i+n]

def la_encipher(string, n):
    alphabet = "abcdefghijklmnopqrstuvwxyzäöüßABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ !\"$%&'()*+,-./:;<=>?@[\]_"
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

def la_decipher(string, n):
    alphabet = "abcdefghijklmnopqrstuvwxyzäöüßABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ !\"$%&'()*+,-./:;<=>?@[\]_"
    res = ""
    for ltr in string:
        if ltr in alphabet:
            decipher_index = alphabet.find(ltr)-n
            if decipher_index < 0:
                res += alphabet[decipher_index+len(alphabet)]
            else:
                res += alphabet[decipher_index]
        else:
            res += ltr
    return res


def la_encipher_key(string, key):
    if len(string) <= len(key):
        return "".join([enciphered for enciphered in map(la_encipher,string,key)])
    else:
        str_segs = sublist(string, len(key))
        res = ""
        for string in str_segs:
            res += "".join([enciphered for enciphered in map(la_encipher,string,key)])
        return res

def la_decipher_key(string, key):
    if len(string) <= len(key):
        return "".join([deciphered for deciphered in map(la_decipher,string,key)])
    else:
        str_segs = sublist(string, len(key))
        res = ""
        for string in str_segs:
            res += "".join([deciphered for deciphered in map(la_decipher,string,key)])
        return res



def zh_encipher(string, n):
    with open("alphabets/zh_shuffled.txt") as zh_alphabet:
        alphabet = zh_alphabet.read()
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


def zh_decipher(string, n):
    with open("alphabets/zh_shuffled.txt") as zh_alphabet:
        alphabet = zh_alphabet.read()
    res = ""
    for ltr in string:
        if ltr in alphabet:
            decipher_index = alphabet.find(ltr)-n
            if decipher_index < 0:
                res += alphabet[decipher_index+len(alphabet)]
            else:
                res += alphabet[decipher_index]
        else:
            res += ltr
    return res


def zh_encipher_key(string, key):
    if len(string) <= len(key):
        return "".join([enciphered for enciphered in map(zh_encipher, string, key)])
    else:
        str_segs = sublist(string, len(key))
        res = ""
        for string in str_segs:
            res += "".join([enciphered for enciphered in map(zh_encipher, string, key)])
        return res


def zh_decipher_key(string, key):
    if len(string) <= len(key):
        return "".join([deciphered for deciphered in map(zh_decipher, string, key)])
    else:
        str_segs = sublist(string, len(key))
        res = ""
        for string in str_segs:
            res += "".join([deciphered for deciphered in map(zh_decipher, string, key)])
        return res


if __name__ == "__main__":
    key = [1, 2, 3]
    sent = input("Enter a message for Caesar: ")
    # encripted_msg = decipher_key(sent,key)
    print(decipher(sent,86))
