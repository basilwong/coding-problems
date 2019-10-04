"""
BCXYZ company has up to

employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.
A valid UID must follow the rules below:

It must contain at least 2 uppercase English alphabet characters.
It must contain at least 3 digits.
It should only contain alphanumeric characters
No character should repeat.
There must be exactly 10 characters in a valid UID.
"""

import re

for _ in range(int(input())):
    imp = input()
    if bool(re.search(r'[a-zA-Z0-9]{10}', imp)) and bool(re.search(r'([A-Z].*){2}', imp)) and \
            bool(re.search(r'([0-9].*){3}', imp)) and not bool(re.search(r'.*(.).*\1', imp)):
        print("Valid")
    else:
        print("Invalid")