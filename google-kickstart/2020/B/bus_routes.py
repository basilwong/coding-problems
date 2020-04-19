
def process_routes(n, x, d):

    for i in range(n-1, -1, -1):
        d = (d // x[i]) * x[i]

    return int(d)



if __name__ =="__main__":
    cases = input()

    for case in range(int(cases)):
        n, d = list(map(int,input().split()))
        x = list(map(int,input().split()))
        print("Case #"+ str(case + 1) + ": " + str(process_routes(n, x, d)))
