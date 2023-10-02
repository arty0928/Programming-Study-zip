# 시작 지점부터 가까운 노드 차례대로 그래프의 모든 노드 탐색

from collections import deque

def bfs(x,y):

    # creating queue
    queue = deque()
    queue.append((x,y))
    # 큐가 빌 때까지 반복
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 미로 범위 내
            if nx<0 or nx >=N or ny <0 or ny >=M:
                continue
            # 괴물이 있는 곳
            if graph[nx][ny]==0:
                continue
            # 1이면 지나갈 수 있고, 처음 지나가는 길이면
            if graph[nx][ny]==1:
                # 그곳을 지나가고 현재 count + 1
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
    
    # 인덱스는 0부터 시작하니까 가장 오른쪽 아랫칸에 도착하면 이때까지의 count return
    return graph[N-1][M-1]
            
    
# 상, 하, 좌, 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

        
N,M =map(int, input().split())  
graph =[]

# 그래프 받기
for i in range(N):
    graph.append(list(map(int,input())))

print(bfs(0,0))