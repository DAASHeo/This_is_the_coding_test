import sys

n = int(sys.stdin.readline().strip())
meeting = []
time = []
count = []
end = 0

for _ in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    meeting.append((x, y))
    time.append((y-x))

for i in len(meeting):
    
