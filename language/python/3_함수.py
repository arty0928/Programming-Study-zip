## 3.1) 함수
    #정의
def f(x):
    result = x+2
    return result

    #호출
print(f(2))
print(f(x=4))

        #dict(my_key=2, 123=456) //(함수의 변수 선언과 같은 원리)dict에서 123을 할 수 없던 이유 -> 함수의 변수명은 문자열이어야 하므로

    #default arguments
def wow_f(x,y,const = 0.1):
    return (x + y) * const 

print(wow_f(3,4))

## 3.4) Return 관련 주의사항
    #return값은 항상 변수로 받아줘야 한다.

print("hi")
def my_func(x,y):
    return x+y
my_func(3,4) #이렇게만 하면 jupyter에서는 7이 출력, 그 외의 환경에서는 return값 출력x


# 3.5) 함수의 4가지 유형
    #1. input O /output O
    #2. input O /output X
    #3. input X /output O
    #4. input X /output X


# 3.6) 함수의 cascading
    #함수를 여러번 선언
def get_my_number():
    return 7

def my_sum(x,y):
    return x+y

print(my_sum(get_my_number(),5))


# 3.7) 함수를 쓰는 이유: 특정 값을 재활용하기 위해(캡슐화)
