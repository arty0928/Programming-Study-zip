# 맨 앞에 있는 원소 = i, 그 이후 배열 중 최소값과 i를 swap
# 앞에서부터 작은 숫자대로 정렬, for문을 배열 끝까지 돔 

# 시간 복잡도: N, N-1, N-2, N-3,,,,2 => O(N의 제곱) 

array = [7,8,4,7,2,1,6,4,3,0]

for i in range(len(array)):
    # 맨 앞에 있는 원소를 최소
    min=i
    for j in range(i+1,len(array)):
        
        # 그 뒤 배열 중 최소값을 찾기
        if(array[min]>array[j]):
            min = j
    
    # 맨 앞에 있는 원소와 배열의 최소값 swap
    array[min], array[i] = array[i],array[min]

print(array)