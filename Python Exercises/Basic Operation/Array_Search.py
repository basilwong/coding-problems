if __name__ == '__main__':
    n = 5
    arr = [2, 3, 6, 6, 5]

    m = arr[0]
    second = -100

    for i in range(1, n):
        # print(m)
        # print(second)
        if arr[i] > m:
            second = m
            m = arr[i]
        elif arr[i] == m:
            continue
        else:
            if arr[i] > second:
                second = arr[i]

    # print('')
    print(second)