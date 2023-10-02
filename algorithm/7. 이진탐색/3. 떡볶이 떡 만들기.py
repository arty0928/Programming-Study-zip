# N,M = map(int,input().split())

# array = list(map(int,input().split()))

# # def find_max(array, N,M):
# #     count = 1
# #     while True:
# #         result = 0
# #         for i in range(N):
# #             tmp = array[i]-count
# #             if tmp > 0:
# #                 result +=tmp
# #         if result == M:
# #             print(count)
# #             break
# #         count +=1

# # find_max(array,N,M)

# count = 0

# def binary_search(array, target, start, end, N, count):
    
#     mid = (start+end)//2
    
#     result=0
#     for i in range(N):
#         tmp = i-mid
#         if tmp >0:
#             result += tmp
    
#     if result >= target:
        
#     elif result >= target:
#         return binary_search(array, target, mid+1, end,N, mid)
#     else:
#         return binary_search(array,target,start,mid-1,N mid)
import sys


def binary_search(array,target,start,end):
    result = 0

    while start <= end:
        print("==========")
        print("result",result)
        total = 0
        mid = (start + end)//2
        print("start mid end",start,mid,end)

        for i in array:
            if i > mid:
                total +=i-mid
        
        
        print("total",total)
        # 떡의 양이 부족한 경우
        if total < target : 
            end = mid - 1
        
        # 떡의 양이 더 많은 경우
        else: 
            start = mid + 1
            # 최댓값
            result = mid 
            
    return result
 
N, M = map(int, input().split())  # Read N and M from standard input (keyboard)
input_lists = list(map(int, input().split()))  # Read the list from standard input

print(binary_search(input_lists,M,0, max(input_lists)))
    
        