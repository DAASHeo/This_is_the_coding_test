def dfs(graph, v, visited):
    visited[v] = True #현재 방문한 노드 방문했다고 표시
    print(v, end=" ")
    for i in graph[v]: # 현재의 노드에서 인접한 노드 방문
        if not visited[i]: # 만약 전에 방문하지 않았다면
            dfs(graph, i, visited) # 방문하러 가기

graph = [ # 그래프 선언
    [],
    [2, 3, 8],
    [1, 7, 8],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * len(graph) # 방문 여부 리스트로 선언

dfs(graph, 1, visited)