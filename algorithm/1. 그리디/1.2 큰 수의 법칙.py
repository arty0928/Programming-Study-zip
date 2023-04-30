from operator import length_hint
from pstats import SortKey


N,M,K = map(int, input().split())
print(N,M,K)
list1 = list(map(int, input().split()))
list2 = [0]*length_hint(list1)
list1.sort(reverse=True)

result = 0

for i in range(M):
    print("range",i,"===========")
    for j in list2:
        if(list2[j]==3):
            print("list2",j,"=",list2[j])
            list2[j]==0
            break
        elif(list2[j]<K):
            print("result +=list2","[",j,"] =",list2[j])
            result += list1[j]
            print("result",result)
            list2[j] +=1
            break

print(result)
