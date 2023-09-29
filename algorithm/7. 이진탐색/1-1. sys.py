# 한 줄 입력받아 출력
import sys

# readlines는 입력 후 엔터가 줄 바꿈 기호로 입력, 공백 문자 제거 위해 rstrip() 사용
input_data = sys.stdin.readlines().rstrip()

print(input_data)