# 시간 복잡도 : O(NlogN) ~ O(N의 제곱)

array = [5,7,9,0,3,1,6,2,4,8]

def quick(array,start,end):
    
    # array에 하나만 남아있다면
    if start >=end:
        return
    
    pivot = start
    left = start + 1
    right = end    
    
    while left<=right:
    
        # pivot보다 큰 숫자가 나올때까지 left + 1
        while left <= end and array[pivot] >= array[left]:
            left +=1
        
        # pivot보다 작은 숫자가 나올때까지 right -1
        # start <= right되면 한개만 남았을때 right-1하면 범위를 벗어나게 됨
        while start < right and array[pivot] <= array[right]:
            right -=1
        
        # 엇갈리면
        if left>right:
            array[right],array[pivot] = array[pivot],array[right]
        
        # 엇갈리지 않았다면 작은 데이터(right), 큰 데이터(left)
        else:
            array[left],array[right] = array[right],array[left]
    
    # pivot이 맨 앞에 있는 원소이니까, 제일 뒤에 있는 원소는 right
    quick(array,start,right-1)
    quick(array,right+1,end)

quick(array, 0, len(array)-1)
print(array)
        