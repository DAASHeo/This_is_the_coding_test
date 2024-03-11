import sys
# n : 물품의 수 ,k : 무게 제한
n, k = map(int, sys.stdin.readline().strip().split())

product = []
d = [0] * (k+1)

for i in range(n):
    product.append(list(map(int, sys.stdin.readline().strip().split())))

for item in product:
    w,v = item
    for i in range(k, w-1, -1):
        d[i] = max(d[i], d[i-w]+v)
print(max(d))