import sys

N = int(input())

input_lists = list(map(int,sys.stdin.readline().split()))

input_lists.sort()

group = 0
N = N-1

while N>0:    
    max = input_lists[N]
    N = N -max
    group +=1

print(group)    
    
    