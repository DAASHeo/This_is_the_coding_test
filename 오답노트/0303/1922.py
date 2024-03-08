import sys
from collections import deque
n = int(input())
m = int(input())
graph = []
computer = [[] for i in range(n)]
money = []
visited = [False] * (n)
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    if a != b:
        graph.append([a,b])
        money.append(c)
        computer[a-1].append(b-1)
        computer[b-1].append(a-1)
    else:
        pass

def bfs(x,y):
    queue = deque([x])
    visited[x] = True
    while queue:
