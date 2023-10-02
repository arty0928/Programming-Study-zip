# 한 줄 입력받아 출력
import sys

# readlines는 입력 후 엔터가 줄 바꿈 기호로 입력, 공백 문자 제거 위해 rstrip() 사용
input_data = sys.stdin.readlines().rstrip()

#📌정해진 개수의 정수를 한줄에 입력받을 때
# map() : 반복 가능한 객체(리스트 등)에 대해 각각의 요소들을 지정된 함수로 처리해주는 함수
a,b,c = map(int,sys.stdin.readline().split())


# 📌 임의의 개수의 정수를 한줄에 입력받아 리스트에 저장할 때
data = list(map(int,sys.stdin.readline().split()))

# 📌 임의의 개수의 정수를 n줄 입력받아 2차원 리스트에 저장할 때
data = []
n = int(sys.stdin.readline())
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))

print(input_data)