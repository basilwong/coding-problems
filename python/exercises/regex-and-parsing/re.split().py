import re

"""
Given a string s consisting only of digits 0-9, commas ,, and dots .
Completes the regex_pattern defined below, which will be used to re.split() all of the , and . symbols in
s.
It’s guaranteed that every comma and every dot in s is preceeded and followed by a digit.
"""


me = (re.split(r".",input()))
for m in me:
   print(m)