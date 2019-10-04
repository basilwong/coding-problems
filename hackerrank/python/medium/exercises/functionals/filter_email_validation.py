"""
Given an integer n followed by n email addresses.
Prints a list containing only valid email addresses in lexicographical order.

Valid email addresses must follow these rules:

- It must have the username@websitename.extension format type.
- The username can only contain letters, digits, dashes and underscores.
- The website name can only have letters and digits.
- The maximum length of the extension is 3.

Example Input:

3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com
"""

import re

def fun(s):
    """
    :param s: inputted email
    :return: True if s is a valid email, else False
    """
    return bool(re.match("^[a-zA-Z][\w-]*@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$", s))



def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)

