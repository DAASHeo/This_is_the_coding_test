import sys
import heapq as hq

n = int(sys.stdin.readline().strip())
meeting = []
for _ in range(n):
    meeting.append(list(map(int, sys.stdin.readline().strip().split())))

meeting.sort(key= lambda x : x[0])

count = 1
pivot = [0]
for start, end in meeting:
    if start >= pivot[0]:
        hq.heappop(pivot)
    else:
        count += 1
    hq.heappush(pivot, end)

print(count)
