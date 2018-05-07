def if_else(n):
    if n%2 != 0:
        return "Weird"
    elif (n >= 2) and (n <= 5):
        return "Not Weird"
    elif (n >= 6) and (n <= 20):
        return "Weird"
    else:
        return "Not Weird"

print (if_else((int(input()))))

def if_else2(n):
    if n%2 != 0:
        print ("Wierd")
    elif (n >= 2) and (n <= 5):
        print ("Wierd")
    elif (n >= 6) and (n <= 20):
        print ("Wierd")
    else:
        print ("Not Wierd")




