from collections import deque

n, m, start = map(int, input().split())

graph = [[] for i in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

def dfs(v):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(start)
visited = [False] * (n+1)
print()
bfs(start)