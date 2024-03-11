t = int(input())

while t > 0 :
    d = [[]] * 41
    n = int(input())
    d[0] = [1, 0]
    d[1] = [0, 1]
    d[2] = [1, 1]

    for i in range(3, n + 1):
        d[i] = [d[i - 1][0] + d[i - 2][0], d[i - 1][1] + d[i - 2][1]]

    print(d[n][0],d[n][1])
    t -= 1