import sys

sys.setrecursionlimit(10**7)
n, m  = map(int, sys.stdin.readline().strip().split())

graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
count = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x):
    visited[x] = True

    for i in graph[x]:
        if not visited[i]:
            dfs(i)


for i in range(1, n+1):
    if visited[i] == True:
        pass
    else:
        dfs(i)
        count += 1

print(count)