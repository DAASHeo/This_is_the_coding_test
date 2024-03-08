from collections import deque

n,m = map(int, input().split())
graph = []
visited = [[0] * m  for _ in range(n)] # 방문 확인
count = [[0] * m  for _ in range(n)]  # 횟수용 리스트 선언

for _ in range(n):
    graph.append(list(map(int, input())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    queue = deque()
    queue.append((0,0))
    visited[0][0] = 1
    count[0][0] = 1

    while queue:

        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    count[nx][ny] = count[x][y] + 1

    return count[n-1][m-1]

print(bfs())