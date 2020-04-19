def in_hole(x, y, l, u, r, d):
    return (x + 1 >= l and x + 1 <= r) and (y + 1 >= u and y + 1 <= d)

def calculated(w, h, l, u, r, d):

    grid = [0.0] * w
    grid[0] = 1.0

    if w == 1 or h == 1:
        return 0.0

    # First row state
    for i in range(0, w - 1):
        if not in_hole(i + 1, 0, l, u, r, d):
            grid[i + 1] += grid[i]

    # Rest of rows
    for y in range(1, h):
        for x in range(0, w):
            # print(x, y)
            if not in_hole(x, y, l, u, r, d):
                if x == 0:
                    grid[x] = grid[x] / 2
                elif x == w - 1:
                    grid[x] = (grid[x - 1] / 2) + (grid[x])
                else:
                    grid[x] = (grid[x - 1] / 2) + (grid[x] / 2)
            else:
                grid[x] = 0

    return grid[-1]

if __name__ =="__main__":
    cases = input()
    for case in range(int(cases)):
        w, h, l, u, r, d = list(map(int,input().split()))
        print("Case #"+ str(case + 1) + ": " + str(calculated(w, h, l, u, r, d)))
