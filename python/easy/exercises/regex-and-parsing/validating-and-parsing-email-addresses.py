"""
Validates whether the input is an email address or not.
"""

import re
import email.utils


n = int(input())
for i in range(n):
    parse = email.utils.parseaddr(input())
    if bool(re.match('[a-zA-Z](\w|-|\.)*@[a-zA-Z]*\.[a-zA-Z]{0,3}$',parse[1])):
        print (email.utils.formataddr(parse))