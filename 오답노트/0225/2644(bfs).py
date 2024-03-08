from collections import deque

n = int(input())
x, y = map(int, input().split())
m = int(input())

graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph: # 요소 크기 순으로 정렬
    i.sort()

dx = [-1,1,0,0]
dy = [0,0,-1,1]

result = 0
def bfs(x, y):
    queue = deque([x])
    global result
    result += 1
    visited[x] = True
    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

    if visited[y] == False
        return print("-1")


bfs(x, y)