N,K = map(int,input().split())
count =0

# 처음 코드
# while(N!=1):
#     R=N%K
#     if(R==0): # + 1
#         N=N/K
#         count = count + 1
#     else:     # + R
#         N=N-R
#         count = count + R
# print(count)


# 두번째 코드(MINE) O(1)
# while N >= K:
#     R = N%K
#     if(R!=0):
#         N-=R
#         count +=R
#     N //=K
#     count +=1

# M = N-1
# N=N-M
# count +=M

# print(count)

#답지 코드 O(1)
while True:
    target = (N//K)*K
    count += N-target
    N =target

    if N<K:
        break
    count += 1
    N//=K

count += N-1
print(count)