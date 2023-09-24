# 깊이 우선 탐색: 시작 노드와 연결된 노드를 깊이있게 우선 탐색
# 동작 원리: 스택
# 구현 방법 : 재귀함수

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited=[False]*9

dfs(graph,1,visited)