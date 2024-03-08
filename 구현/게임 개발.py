n, m = map(int, input().split())
land = []
visited = [[False] * m for i in range(n)]
x, y, z = map(int, input().split())
for _ in range(n):
    land.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited[x][y] = True
count = 0 # 거쳐간 칸 갯수 변수
turn_count = 0 # 회전 횟수 변수

def direction():
    global z
    z -= 1
    if z == -1:
        z = 3

while True:
    direction()
    nx = x + dx[z]
    ny = y + dy[z]
    if visited[nx][ny] == False and land[nx][ny] == 0:
        visited[nx][ny] = True
        x = nx
        y = ny
        count += 1
        turn_count = 0
        continue
    else:
        turn_count += 1

    if turn_count == 4:
        nx = x - dx[z]
        ny = y - dy[z]

        if land[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_count = 0

print(count)


