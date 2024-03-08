n, m, k = map(int, input().split())
graph = []
graph = list(map(int, input().split()))
check = graph.count(max(graph))
graph.sort(reverse=True)


result = 0
state = 0

if check >= 2:
    result = m * max(graph)
else:
    for _ in range(m):
        if state == k:
            result += graph[1]
            state = 0
        else:
            result += graph[0]
            state += 1

print(result)