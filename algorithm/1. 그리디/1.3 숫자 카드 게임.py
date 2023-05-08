N,M =map(int, input().split())

result = 0

for i in range(N):
    data = map(int, input().split())

    minimal = 10001
    for x in data:
        minimal = min(x,minimal)
    result = max(minimal,result)

print(result)

