# 이진탐색: O(logN)

total_count, target = map(int,input().split())
lists = list(map(int,input().split()))

def binary_search(array,target,start,end):
    if start>end:
        return None
    
    mid = (start+end)//2
    
    print(start,mid,end)
    
    if array[mid]==target:
        return mid
    elif array[mid]>target:
        print("target 더 작음")
        return binary_search(array,target,start,mid-1)
    else:
        print("target 더 큼")
        return binary_search(array,target,mid+1,end)


result = binary_search(lists,target,0,total_count-1)

if result==None:
    print("찾을 수 없습니다")
else:
    print(result+1)

