# dfs는 부모 노드 -> 자식 노드로 이동함
import sys

sys.setrecursionlimit(10**6)

n = int(input())

graph = [[] for i in range(n+1)]

visited = [0]*(n+1)

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x):
    for i in graph[x]:
        if not visited[i]:
            visited[i] = x # 방문 리스트에 현재 이 노드의 상위 노드를 저장
            dfs(i)

dfs(1)

for i in range(2,n+1):
    print(visited[i])

