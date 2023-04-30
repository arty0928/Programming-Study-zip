number = int(input())
grade = list(map(int, input().split()))
mean =0

max = grade[0]

for i in grade:
    if max < i:
         max = i

for i in grade:
     mean +=i / max *100

print(mean/number)