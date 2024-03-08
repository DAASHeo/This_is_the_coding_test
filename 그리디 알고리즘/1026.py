import sys

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))
b = list(map(int, sys.stdin.readline().strip().split()))
result = 0


for i in range(n):
    x = a.pop(a.index(min(a)))
    y = b.pop(b.index(max(b)))
    result += x * y

print(result)