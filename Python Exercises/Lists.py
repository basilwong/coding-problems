# insert i e: Insert integer
#
# at position
#
# .
# print: Print the list.
# remove e: Delete the first occurrence of integer
#
# .
# append e: Insert integer
#
# at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.

import sys

def list_commands(line, command):
    line_parts = command.split()
    if line_parts[0] == "insert":
        line.insert(int(line_parts[1]), int(line_parts[2]))
    elif line_parts[0] == "print":
        print (line)
    elif line_parts[0] == "remove":
        line.remove(int(line_parts[1]))
    elif line_parts[0] == "append":
        line.append(int(line_parts[1]))
    elif line_parts[0] == "sort":
        line.sort()
    elif line_parts[0] == "pop":
        line.pop()
    elif line_parts[0] == "reverse":
        line.reverse()
    else:
        print ("issue")

product = []

numbers = int(input())

for i in range(1,numbers+1):
    nextLine = input()
    list_commands(product, nextLine)