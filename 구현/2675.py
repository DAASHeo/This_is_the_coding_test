t = int(input())
while(t != 0):
    m, n = input().split()
    for i in range(len(n)):
        print(n[i] * int(m), end='')
    print('')
    t -= 1