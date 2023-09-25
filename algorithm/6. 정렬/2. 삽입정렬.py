# 특정 데이터를 적절한 위치에 삽입 
# 적절한 위치 앞까지는 이미 정렬 완료

# 시간 복잡도 : O(N) ~ O(N의 제곱) 
# 이미 거의 정렬된 경우에는 O(N)로 퀵 정렬보다 빠르다

array = [7,8,4,7,2,1,6,4,3,0]

for i in range(len(array)):
    # i부터 1까지 -1씩 감소
    for j in range(i,0,-1):
        if array[j]<array[j-1]:
            array[j],array[j-1] = array[j-1],array[j]
        
        # 자기보다 크거나 같으면 멈춤
        else:
            break

print(array)
