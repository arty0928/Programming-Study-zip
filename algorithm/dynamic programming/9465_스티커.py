# 횟수
T = int(input())

N =int(input()) # 열 개수

# 열 입력 받기
arr = [list(map(int, input().split())) for _ in range(2)]
print(arr)

# 선택한 숫자 넣기
result =0
#선택한 행, 열

# 위아래 중 큰 수 선택
# if arr[0][0] > arr[1][0]:
#     big = arr[0][0]
#     x = 0
#     y = 0 
# else:
#     big = arr[1][0]
#     x = 1
#     y = 0

# 위 아래 중 더 큰 숫자 찾기
if(arr[0][0] > arr[1][0]):
    result += arr[0][0]
else:
    result += arr[1][0]

for i in N:
    #대각선 선택
        # y+z >=w
    if(arr[1][i+1]+arr[0][i+2] >= arr[1][i+2]):   
        result += arr[1][i+1]+arr[0][i+2]
        i = i+3

    #선택x -> 그 다음 열 선택 
        # y+ z < w
    else:
        arr[0][i]
