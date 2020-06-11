import heapq

def plates(n, k, p, stacks):

    max_heap = list()

    frontier = max(k, p)
    for stack in stacks:
        for i in range(1, frontier):
            stack[i] = ((stack[i - 1] * i) + stack[i]) / (i + 1)

if __name__ =="__main__":
    cases = input()

    for case in range(int(cases)):
        n, k, p = list(map(int,input().split()))
        stacks = list()
        for _ in range(n):
            stacks.append(list(map(int,input().split())))
        print("Case #"+ str(case + 1) + ": " + str(plates(n, k, p, stacks)))
