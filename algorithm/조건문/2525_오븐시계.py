h,m = map(int, input().split())
time = int(input())

m = m + time
h = h + m//60 #몫
m = m % 60  #나머지

if(h >= 24):
    h = h - 24

print(h,m)