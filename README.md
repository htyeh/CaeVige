# CaeVige (Caesar-Vigenère) Encryption/Decryption Tool: Usage Guide

## Encipher a single Latin or Chinese text
python3 la_encipher.py -k ***key_name***.txt -f ***filename***.txt -o ***output_name***.txt
python3 zh_encipher.py -k ***key_name***.txt -f ***filename***.txt -o ***output_name***.txt

## Decipher a single Latin or Chinese text
python3 la_decipher.py -k ***key_name***.txt -f ***filename***.txt -o ***output_name***.txt
python3 zh_decipher.py -k ***key_name***.txt -f ***filename***.txt -o ***output_name***.txt

## Brute force an encrypted file
python3 brute_force.py -f ***encrypted_file***.py

## Efficient key search with Kasiski method
python3 kasiski_crack.py -f ***encrypted_file***.py