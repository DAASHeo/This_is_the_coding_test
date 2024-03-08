from collections import deque
import sys

n, k = map(int, input().split())
time = 0
visited = [False] * 100001

def bfs(x, y):
    global time
    queue = deque([x])
    visited[x] = 0
    while (queue):
        current = queue.popleft()
        if current == k:
            return visited[current]
        for i in (1+current, current-1, 2*current):
            if 0 <= i <= 100000 and not visited[i]:
                if i == current * 2:
                    visited[i] = visited[current]
                    queue.appendleft(i)
                else:
                    visited[i] = visited[current] + 1
                    queue.append(i)

    return print(time)

bfs(k)