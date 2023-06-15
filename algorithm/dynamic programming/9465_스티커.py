# 횟수
T = int(input())

# for i in T:

N =int(input()) # 열 개수

arr = [list(map(int, input().split())) for _ in range(2)]
print(arr)

# 선택한 숫자 넣기
selected=[]
#선택한 행, 열

# 위아래 중 큰 수 선택
if arr[0][0] > arr[1][0]:
    big = arr[0][0]
    x = 0
    y = 0 
else:
    big = arr[1][0]
    x = 1
    y = 0

print(big)
