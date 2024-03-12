import sys
k = int(sys.stdin.readline().strip())
record = []
for _ in range(k):
    n = sys.stdin.readline().strip()
    if n == "0":
        record.pop()
    else:
        record.append(int(n))

print(sum(record))