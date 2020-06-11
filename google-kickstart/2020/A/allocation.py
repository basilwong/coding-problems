import heapq

def max_houses(n, b, points):
    heapq.heapify(points)
    count = 0
    price = 0
    while points:
        price += heapq.heappop(points)
        count += 1
        if price < b:
            return count - 1
    return count

if __name__ =="__main__":
    cases = input()

    for case in range(int(cases)):
        n, b = list(map(int,input().split()))
        points = list(map(int,input().split()))
        print("Case #"+ str(case + 1) + ": " + str(max_houses(n, b, points)))
