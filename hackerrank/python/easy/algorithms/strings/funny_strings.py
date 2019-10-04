import os

# Complete the funnyString function below.
def funnyString(s):
    n = len(s)
    for i in range(n - 1):
        print(i)
        begin = abs(ord(s[i]) - ord(s[i + 1]))
        ended = abs(ord(s[n - i - 1]) - ord(s[n - i - 2]))
        if begin != ended:
            return 'Not Funny'
    return 'Funny'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
