# 토마토 하루 지나면 익음
# 정수 1은 익은 토마토,
# 정수 0 은 익지 않은 토마토,
# 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.

import sys
from collections import deque

m, n, h = map(int, input().split())
arr = []
que = deque([])
day = 0
for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, sys.stdin.readline().split())))
        for k in range(m):
            if tmp[j][k] == 1:
                que.append([i, j, k])  # 익은 토마토 위치
    arr.append(tmp)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while que:
    x, y, z = que.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and arr[nx][ny][nz] == 0:
            que.append([nx, ny, nz])
            arr[nx][ny][nz] = arr[x][y][z] + 1

for i in arr:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
            day = max(day, max(j))

print(day - 1)
