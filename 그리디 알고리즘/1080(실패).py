import sys

n, m = map(int, sys.stdin.readline().strip().split())

a = []
b = []

for _ in range(n):
    a.append(list(map(int, sys.stdin.readline().strip().split())))

for _ in range(n):
    b.append(list(map(int, sys.stdin.readline().strip().split())))

if n < 3 or m < 3:
    if a != b:
        print("-1")

    else:
        print("0")
