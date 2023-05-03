from operator import length_hint

N,M,K = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = [0]*length_hint(list1)
list1.sort(reverse=True)
result = 0

for i in range(M):
    for j in range(len(list2)):
        if(list2[j]< K):
            print("result +=list2","[",j,"] =",list2[j], list1[j])
            result +=list1[j]
            list2[j] +=1
            break
        elif(list2[j] == 3):
            print(j, list2[j])
            list2[j]=0

print(result)
