
## -- MINE CODE
# from operator import length_hint

# N,M,K = map(int, input().split())
# list1 = list(map(int, input().split()))
# list2 = [0]*length_hint(list1)
# list1.sort(reverse=True)
# result = 0

# for i in range(M):
#     for j in range(len(list2)):
#         if(list2[j]< K):
#             print("result +=list2","[",j,"] =",list2[j], list1[j])
#             result +=list1[j]
#             list2[j] +=1
#             break
#         elif(list2[j] == 3):
#             print(j, list2[j])
#             list2[j]=0

# print(result)


## -- 해설 확인 후 코드 다시 작성
# 시간복잡도가 O(n)이 되려면 
N,M,K = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)
print(data)

first = data[0] #max
second = data[1] #그 다음 max

#max가 더해지는 횟수
count = K*(M/(K+1)) + M % (K+1)

result = 0
result += count * first
result += (M-count) * second

print(result)
