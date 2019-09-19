############################### README ###############################
# usage exp.: python3 decipher.py -k key_doc.txt -f to_be_deciphered_doc.txt -o output.txt
######################################################################

from main import la_decipher, la_decipher_key
import sys
import os
import time
import argparse
import datetime

start_time = time.time()

parser = argparse.ArgumentParser(description="DECIPHER TEXT FILE")
parser.add_argument("-k", "--key", help="Specify key file.", required=True)
parser.add_argument("-f", "--file", help="Specify file to be decrypted.", required=True)
parser.add_argument("-o", "--output", help="Specify optional output file name.")
args = parser.parse_args(sys.argv[1:])

with open(args.key) as key_file:
    key = [int(i) for i in key_file.read().split()]

with open(args.file) as msg_file:
    msg = msg_file.read()

deciphered_msg = la_decipher_key(msg,key)

if args.output:
    with open(args.output,"w") as output:
        output.write(deciphered_msg+"\n")
else:
    with open("deciphered " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ".txt", "w") as output:
        output.write(deciphered_msg+"\n")

end_time = time.time()
print(args.file + " (" + str(len(msg)) + " char(s)) decrypted in " + str(round(end_time-start_time, 2)) + " second(s).")
