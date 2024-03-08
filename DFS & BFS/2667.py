import sys
sys.setrecursionlimit(100000)
n = int(sys.stdin.readline())

graph = [] * n
visited = [[False] * n for i in range(n)]
count = 0 # 총 단지 수
home = 0# 단지 내 가구 수
home_list = []

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().strip())))

def dfs(x, y):
    global home
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        home += 1
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

for i in range(n):
    for j in range(n):
        home = 0
        if dfs(i, j) == True:
            home_list.append(home)
            count += 1

print(count)
home_list.sort()
for i in home_list:
    print(i)