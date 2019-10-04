from collections import deque

def shortest_reach_bfs(n, s, arr):

    # Create graph representation using sets
    storage = [set() for _ in range(n)]
    for p in arr:
        storage[p[0]].add(p[1])
        storage[p[1]].add(p[0])

    ret = [-1] * n
    ret[s] = 0
    queue = deque()
    queue.append(s)

    # Implement bfs
    while queue:
        cur = queue.popleft()
        for x in storage[cur]:
            if ret[x] == -1:
                ret[x] = ret[cur] + 6
                queue.append(x)

    del ret[s]
    return ret


if __name__ == "__main__":
    queries = int(input())
    for _ in range(queries):
        n, m = input().split()
        n = int(n)
        m = int(m)
        arr = list()
        for _ in range(m):
            a, b = input().split()
            arr.append([int(a) - 1, int(b) - 1])
        s = int(input()) - 1
        print(' '.join(map(str, shortest_reach_bfs(n, s, arr))))
