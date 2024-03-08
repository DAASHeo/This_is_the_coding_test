from collections import deque

n, m, t = map(int, input().split())
graph =[]

for _ in range(n):
    graph.append(list(map(int, input().split())))


count = [[0]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)]
weapon = False

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    global weapon
    queue = deque()
    queue.append((0,0))
    visited[0][0] = 1
    count[0][0] = 1

    while (queue):
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < n and nx >= 0 and ny < m and ny >= 0:
                if graph[nx][ny] == 2 and visited[nx][ny] == 0:
                    weapon = True
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    count[nx][ny] = count[x][y] + 1
                elif weapon == False and graph[nx][ny] == 0 and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    count[nx][ny] = count[x][y] + 1
                elif weapon == True and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    count[nx][ny] = count[x][y] + 1

    if count[n-1][m-1] - 1 > t or count[n-1][m-1] == 0:
        return "Fail"
    else:
        return count[n-1][m-1] - 1

case1 = 0
case2 = 0
if
print(bfs())
