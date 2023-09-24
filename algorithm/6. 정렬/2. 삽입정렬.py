# 특정 데이터를 적절한 위치에 삽입 
# 적절한 위치 앞까지는 이미 정렬 완료

array = [7,8,4,7,2,1,6,4,3,0]

for i in range(1, len(array)):
    for j in range(len(array)):
        v = array.pop(array[i])
        if(array[j]<v and v<array[j+1]):
            array.insert(j,v)
    array.insert(j,v)

print(array)
