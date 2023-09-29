N,M = map(int,input().split())

array = list(map(int,input().split()))

def find_max(array, N,M):
    count = 1
    while True:
        result = 0
        for i in range(N):
            tmp = array[i]-count
            if tmp > 0:
                result +=tmp
        if result == M:
            print(count)
            break
        count +=1

find_max(array,N,M)
    
                