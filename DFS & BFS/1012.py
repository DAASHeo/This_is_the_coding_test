import sys
#파이썬의 최대 재귀 깊이는 1000임. 문제의 조건인 50 * 50 = 2500까지 진행하려면 재귀 깊이 제한을 변경해야함
sys.setrecursionlimit(10000)

t = int(input())

for _ in range(t):

    m, n, v = map(int, input().split())

    graph = [[0]*m for i in range(n)]

    for _ in range(v):
        a,b = map(int, input().split())
        graph[b][a] = 1


    def dfs(x, y):
        if x <= -1 or x >= m or y <= -1 or y >= n:
            return False
        if graph[y][x] == 1:
            graph[y][x] = 0
            dfs(x-1, y)
            dfs(x, y-1)
            dfs(x+1, y)
            dfs(x, y+1)
            return True
        return False


    result = 0
    for i in range(m):
        for j in range(n):
            if dfs(i,j) == True:
                result += 1

    print(result)
