# CaeVige (Caesar-Vigenère) Encryption/Decryption Tool: Usage Guide

## Encipher a single Latin or Chinese text
python3 la_encipher.py -k ***key_name***.txt -f ***filename***.txt -o ***output_name***.txt

python3 zh_encipher.py -k ***key_name***.txt -f ***filename***.txt -o ***output_name***.txt

## Decipher a single Latin or Chinese text
python3 la_decipher.py -k ***key_name***.txt -f ***filename***.txt -o ***output_name***.txt

python3 zh_decipher.py -k ***key_name***.txt -f ***filename***.txt -o ***output_name***.txt

## Brute-force
Brute-force takes in the estimated key length and the strength of each bit and tries every possible key in order to find the most likely key. By default, 20% of the decrypted text must exist in the dictionary file, and
85% of all the characters in the decrypted text must be letters or spaces.

Usage: python3 brute_force.py -f ***encrypted_file***.py

## Efficient key search with Kasiski method
Possible key lengths can be estimated by capturing repeating patterns in encrypted texts and calculating factors of the results. These lengths are ranged by frequencies. Furthermore, the number of keys to for trial is greatly reduced by cutting each list (of keys of a certain length) to a user-determined length (default 3) using frequency analysis.

Usage: python3 kasiski_crack.py -f ***encrypted_file***.py