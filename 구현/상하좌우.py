n = int(input())

graph=[[0] * n for i in range(n)]
x,y = 1, 1 #현재 위치
move = list(map(str, input().split()))
direction = ["L","R","U", "D"]

dx = [-1,1,0,0]
dy = [0, 0, -1, 1]

for i in move:
    for j in range(len(direction)):
        if i == direction[j]:
            if (0 < x + dx[j] <= n and 0 < y + dy[j] <= n):
                x = x + dx[j]
                y = y + dy[j]
            else:
                pass


print(y, x)