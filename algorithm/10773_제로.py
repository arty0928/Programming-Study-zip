import sys
times = int(sys.stdin.readline())

line = []
rest = 0

for i in range(times):
    a = int(sys.stdin.readline())
    if a==0:
        line.pop()
    else:
        line.append(a)

for j in line:
    rest += j

print(rest)