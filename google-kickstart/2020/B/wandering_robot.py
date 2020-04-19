def in_hole(x, y, l, u, r, d):
    return (x + 1 >= l and x + 1 <= r) and (y + 1 >= u and y + 1 <= d)

def calculated(w, h, l, u, r, d):

    grid = [[0.0] * w for _ in range(h)]
    grid[0][0] = 1.0

    # Rest of rows
    for x in range(0, len(grid[0]) - 1):
        for y in range(0, len(grid) - 1):
            # print(x, y)
            if not in_hole(x + 1, y, l, u, r, d):
                grid[y][x + 1] += grid[y][x] / 2
            if not in_hole(x, y + 1, l, u, r, d):
                grid[y + 1][x] += grid[y][x] / 2

    # Process first row
    for i in range(0, len(grid[0]) - 1):
        if not in_hole(i + 1, len(grid) - 1, l, u, r, d):
            grid[len(grid) - 1][i + 1] += grid[len(grid) - 1][i]

    # Process last column
    for i in range(0, len(grid) - 1):
        if not in_hole(len(grid[0]) - 1, i + 1, l, u, r, d):
            grid[i + 1][len(grid[0]) - 1] += grid[i][len(grid[0]) - 1]

    # print(grid)

    return grid[-1][-1]
if __name__ =="__main__":
    cases = input()
    for case in range(int(cases)):
        w, h, l, u, r, d = list(map(int,input().split()))
        print("Case #"+ str(case + 1) + ": " + str(calculated(w, h, l, u, r, d)))
