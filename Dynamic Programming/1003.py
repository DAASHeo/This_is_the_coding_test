def fibo(x):
    print("x:",x)
    if x == 1 or x == 2:
        count[x] += 1
        return 1
    if x == 0 :
        count[x] += 1
        return 0
    if d[x] != 0:
        return d[x]
    else:
        d[x] = fibo(x-1) + fibo(x-2)

t = int(input())

while t > 0 :
    d = [0] * 41
    count = [0] * 3
    n = int(input())
    fibo(n)
    print(count[0],count[1])
    t -= 1