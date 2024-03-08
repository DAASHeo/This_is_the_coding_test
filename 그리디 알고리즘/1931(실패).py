import sys

n = int(sys.stdin.readline().strip())
time = []

for _ in range(n):
    time.append(list(map(int, sys.stdin.readline().strip().split())))

time = sorted(time, key= lambda start : (start[1],start[0]))

pivot = time[0][1]
count = 1
for i in range(1, n):
    if pivot <= time[i][0]:
        count += 1
        pivot = time[i][1]

print(count)