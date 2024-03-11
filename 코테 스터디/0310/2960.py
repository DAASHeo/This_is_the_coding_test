import sys
n,k = map(int, sys.stdin.readline().strip().split())

d = [i for i in range(2,n+1)]
count = []
num = 0

while (len(d) != 0):
    p = d.pop(d.index(min(d)))
    count.append(p)
    for i in d:
        if i % p == 0:
            num = d.pop(d.index(i))
            count.append(num)

print(count[k-1])
