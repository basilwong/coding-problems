from scipy.special import comb

def calculated(w, h, l, u, r, d):

    ans = 0

    # Bottom left:
    row = d
    col = l - 2
    while row < h and col >= 0:
        if row == h - 1 or col == 0:
            ans += 0.5**(row + col)
        else:
            ans += 0.5**(row + col) * comb(row + col, col)
        row += 1
        col -= 1

    # Top Right:
    row = u - 2
    col = r
    while row >= 0 and col < w:
        if row == 0 or col == w - 1:
            ans += 0.5**(row + col)
        else:
            ans += 0.5**(row + col) * comb(row + col, col)
        row -= 1
        col += 1

    return ans


if __name__ =="__main__":
    cases = input()
    for case in range(int(cases)):
        w, h, l, u, r, d = list(map(int,input().split()))
        print("Case #"+ str(case + 1) + ": " + str(calculated(w, h, l, u, r, d)))
