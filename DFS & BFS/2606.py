n = int(input()) #컴퓨터의 갯수
m = int(input()) # 연결선의 갯수
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
result = 0

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    global result
    visited[start] = True
    result += 1
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

    return result

print(dfs(1)-1)