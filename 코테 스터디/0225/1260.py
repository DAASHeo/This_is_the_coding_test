from collections import deque
import sys

sys.setrecursionlimit(10000) # 파이썬 재귀 깊이 디폴트 1000이라서 10000으로 조정

n, m, v = map(int, input().split())

graph = [[] for i in range(n+1)] # 그래프 생성
visited = [False] * (n+1) # 방문 여부 배열 생성

for i in range(m): # 각각의 노드 연결
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph: # 요소 크기 순으로 정렬
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


dfs(v)
visited = [False] * (n+1) # 방문 기록 초기화
print(" ")
bfs(v)