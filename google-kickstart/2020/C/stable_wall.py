import collections

def traverse(row, column, grid, value):
    if row < 0 or row >= len(grid) or column < 0 or column >= len(grid[0]) or grid[row][column] != value:
        return {}
    dependencies = set()
    if row < len(grid) - 1 and (grid[row + 1][column] != value or grid[row + 1][column] != value.lower()):
        dependencies.add(grid[row + 1][column].lower())
    grid[row][column] = value.lower()
    dependencies.update(traverse(row, column - 1, grid, value))
    dependencies.update(traverse(row, column + 1, grid, value))
    dependencies.update(traverse(row - 1, column, grid, value))
    dependencies.update(traverse(row + 1, column, grid, value))
    # if value == "O":
    #     print(row, column, dependencies)
    return dependencies

def find_order(dic):
    neigh = collections.defaultdict(set)
    for k, v in dic.items():
        for val in v:
            neigh[val].add(k)
    # queue stores the courses which have no prerequisites
    queue = collections.deque([k for k, v in dic.items() if not v])
    count, res = 0, []
    while queue:
        node = queue.popleft()
        # print("Node:", node)
        # print("Queue:", queue)
        # print("Dic:", dic)
        # print("Neigh:", neigh)
        res.append(node.upper())
        count += 1
        for i in neigh[node]:
            dic[i].remove(node)
            if not dic[i]:
                queue.append(i)
    return "".join(res) if count == len(dic) else "-1"

def stable(r, c, grid):
    dependencies = dict()

    for row in range(r - 1, -1, -1):
        for column in range(c):
            if grid[row][column] not in dependencies:
                dependencies[grid[row][column]] = traverse(row, column, grid, grid[row][column]) - { grid[row][column] }
    # print(dependencies)
    return find_order(dependencies)



if __name__ =="__main__":
    cases = input()

    for case in range(int(cases)):
        r, c = list(map(int,input().split()))
        grid = list()
        for _ in range(r):
            grid.append(list(input()))
        print("Case #"+ str(case + 1) + ": " + stable(r, c, grid))
