def countdown(n, k, arr):

    count = 0
    state = k
    for i in range(n):
        print(state, count)
        if arr[i] == state:
            if state == 1:
                count += 1
                state = k
            else:
                state -= 1
        elif arr[i] == k:
            state = k - 1
        else:
            state = k

    return count


if __name__ =="__main__":
    cases = input()

    for case in range(int(cases)):
        n, k = list(map(int,input().split()))
        points = list(map(int,input().split()))
        print("Case #"+ str(case + 1) + ": " + str(countdown(n, k, points)))
