

def find_peaks(n, points):
    count = 0
    for i in range(1, n-1):
        if points[i] > points[i-1] and points[i] > points[i+1]:
            count += 1
    return count



if __name__ =="__main__":
    cases = input()

    for case in range(int(cases)):
        n = int(input())
        points = list(map(int,input().split()))
        print("Case #"+ str(case + 1) + ": " + str(find_peaks(n, points)))
