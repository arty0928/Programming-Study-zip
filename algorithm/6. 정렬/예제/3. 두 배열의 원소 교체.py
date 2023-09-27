array_length,count = map(int,input().split())

# map: 반복 가능한 객체(리스트, 튜플 등) 의 요소에 대해 어떤 함수를 일괄 적용
    # map 사용 예제
        # numbers = [1,2,3]
        # result = map(square,numbers) #result = [1,4,9]

A = list(map(int,input().split()))
B = list(map(int,input().split()))

print(A)
print(B)

A.sort()
B.sort(reverse=True)

for i in range(count):
    if (A[i]<B[i]):
        A[i],B[i]=B[i],A[i]


print(A)
print(B)
print(sum(A))