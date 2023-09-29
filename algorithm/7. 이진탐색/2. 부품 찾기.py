
total = int(input())

lists = list(map(int, input().split()))

find_count = int(input())

find_lists = list(map(int, input().split()))

lists.sort()

def binary_search(array,target, start,end):
    if start > end:
        return -1
    mid =(start+end)//2
    
    if array[mid]==target:
        return 1
    elif array[mid] > target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)

result_lists =[]

for i in find_lists:
    result = binary_search(lists, i, 0, len(lists)-1)
    if result == 1:
        # result_lists.append("yes")6
        print("yes",end=' ')
    else:
        print("no", end=' ')
        # result_lists.append("no")

    