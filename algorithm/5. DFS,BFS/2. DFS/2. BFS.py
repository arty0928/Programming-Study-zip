# 너비 우선 탐색(Breadth first search): 시작 노드와 가까운 노드부터 우선 탐색, 소요시간 O(N) dfs보다 빠름
# 동작원리 : 큐
# 구현방법 : 큐 자료구조 이용 (deque) -> 선입선출 (먼저 들어온 것 먼저, 가까운 것 먼저)

from collections import deque

def bfs(graph, start, visited):
    # 현재 노드 방문 처리
    visited[start] = True
    # creating queue
    queue = deque([start])
    
    
    # queue를 돌면서
    while queue:
        
        # 현재 방문한 노드를 출력
        v = queue.popleft()
        print(v, end=' ')
        
        # 현재 방문한 노드와 인접한 노드들 중
        for i in graph[v]:
            # 방문 안 한 노드는 append
            if not visited[i]:
                queue.append(i)
                visited[i]=True    
    
graph=[
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

visited = [False] * 9


bfs(graph,1,visited)