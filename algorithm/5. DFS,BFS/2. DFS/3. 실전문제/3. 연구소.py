from collections import deque

def bfs(x,y):
    queue = deque()
    

N,M = map(int, input().split())
array =[]


for i in range(N):
    array.append(list(map(int,input().split())))

print(array)