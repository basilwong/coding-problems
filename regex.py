

def regex(s, p):
    i = 0 # s index
    j = 0 # j index
    while i < len(s) and j < len(p):
        if p[j] == "*":
            return handle_star_recursive(s[i - 1], s[i:], p[j:])
        elif p[j] != "." and p[j] != s[i]:
            return False
        i += 1
        j += 1
    while j < len(p):
        if p[j] == "*":
            j += 1
        else:
            break
    return i == len(s) and j == len(p)

def handle_star_recursive(c, s, p):
    if c == s[0]:
        if len(s) == 1:
            if len(p) == 1:
                return True
            else:
                return regex(s, p[1:])
        else:
            if len(p) == 1:
                return handle_star_recursive(c, s[1:], p)
            else:
                return regex(s, p[1:]) or handle_star_recursive(c, s[1:], p)
    else:
        if len(p) == 1:
            return False
        else:
            return regex(s, p[1:])

if __name__ == "__main__":
    print(regex("aab", "c*a*b"))
