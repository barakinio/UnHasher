# Imports
import argparse
import hashlib

# Constants
DESC = "Unhashes an md5 hash with a wordlist"
PHELP = "path for wordlist"
VHELP = "value to unhash"
PASCOR = "IS the password!"
PASBAD = "is not the password...\n"


def main():
    parser = argparse.ArgumentParser(description=DESC)
    parser.add_argument("-p", "--path", type=str, help=PHELP)
    parser.add_argument("-v", type=str, help=VHELP)
    args = parser.parse_args()

    # Opens the word list file ans saves every line to a list.
    with open(args.path, "r") as wordlistfile:
        wordlist = wordlistfile.read().splitlines()

    # Runs on every possible password, hashes it and compares to the given hash value.
    # If the hashes are equal, we will print the correct password and break from the loop.
    # If the hases are not equal, we will print and continue to the next attempt.
    for pswd in wordlist:
        print (password, end =" ")
        pswdhash = hashlib.md5(pswd.encode('utf-8')).hexdigest()
        print (PASCOR) if pswdhash == args.v else print (PASBAD)

if __name__ == "__main__":
    main()
