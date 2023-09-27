number = int(input())
lists=[]

for i in range(number):
    lists.append( int(input()) )

lists.sort(reverse=True)


for i in lists:
    print(i, end=' ')