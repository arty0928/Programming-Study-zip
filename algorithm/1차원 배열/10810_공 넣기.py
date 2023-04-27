M,N = map(int, input().split())
M = [0]*M #초기화안하면 M은 int형이라 배열로 넣을 수 없음

def putball(start,end,number):
    for i in range(start,end+1): #end전의 숫자까지 range라서 +1
        M[i] = number 

for i in range(N):
    start,end,number = map(int, input().split())
    putball(start-1,end-1,number)

for i in M:
    print(i)