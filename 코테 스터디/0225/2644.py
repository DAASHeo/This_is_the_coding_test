n = int(input())
num1,num2 = map(int, input().split())
m = int(input())

graph = [[] for i in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

result = []
def dfs(x, num):
    visited[x] = True

    if x == num2:
        return result.append(num)

    num += 1

    for i in graph[x]:
        if not visited[i]:
            dfs(i, num)

dfs(num1, 0)

if len(result) == 0:
    print("-1")
else:
    print(result[0])

