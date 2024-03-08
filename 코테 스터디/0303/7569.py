#dfs 문제가 아니라 bfs로 풀어야했다고 함
# 정수 1 : 익은 토마토, 정수 0 : 익지 않은 토마토, 정수 -1 : 토마토 없음
import sys
from collections import deque
n, m = map(int, sys.stdin.readline().strip().split())

graph = []
days = []
flag = False
zero_days = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(m):
    graph.append(list(map(int, sys.stdin.readline().strip().split())))

def bfs():
    queue = deque()
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                queue.append((i,j,0))

    max_day = 0
    while queue:
        x,y,day = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n  and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                next_day = day + 1
                queue.append((nx, ny, next_day))
                max_day = max(max_day, next_day)

    for i in range(m):
        for j in range(n):
            if graph[i][j] == 0:  # 익지 않은 토마토가 있는 경우
                return -1
    return max_day

print(bfs())
