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
                if visited[nx][ny] == 0:
                    if graph[nx][ny] == 2:
                        weapon = True
                        queue.append((nx, ny))
                        visited[nx][ny] = 1
                        count[nx][ny] = count[x][y] + 1
                    if graph[nx][ny] == 0:
                        queue.append((nx, ny))
                        visited[nx][ny] = 1
                        count[nx][ny] = count[x][y] + 1

    print(count[n-1][m-1] - 1)
    return count[n-1][m-1] - 1

case1 = 0
case2 = 0

if weapon == True:
    graph = [[0] * m for i in range(n)]
    case2 = bfs()

print(case1, case2)

if case1 > t and case2 > t:
    print("Fail")
elif case1 == 1 and case2 == 1:
    print("Fail")
else:
    print(min(case1,case2))


"""
실패인 경우:
t보다 큰 경우
count[n - 1][m - 1] == 0 인 경우
"""
