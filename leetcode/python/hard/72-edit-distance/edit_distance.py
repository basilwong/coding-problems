def helper(w1, w2, cur):
    i = 0
    j = 0
    while i < len(w1) and j < len(w2):
        if w1[i] != w2[j]:
            return min(helper(w2[j] + w1[i:], w2[j:], cur + 1), helper(w1[i+1:], w2[j:], cur + 1), helper(w2[j] + w1[i+1:], w2[j:], cur + 1))

        i += 1
        j += 1


    if i < len(w1):
        return len(w1) - i + cur
    elif j < len(w2):
        return len(w2) - j + cur
    else:
        return cur

print(helper("dinitrophenylhydrazine", "acetylphenylhydrazine", 0))
