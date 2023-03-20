## 2.2) 리스트 (list)
    # list가 필요한 이유
        # 한 학급의 성적을 관리할때, 변수를 많이 만들 필요없이, 번호를 부여 (=array)

class_score = [90,30,60]
class_score = [1,2,[3,4]]

    # indexing
        # 0부터 시작하는 이유
            # list의 변수명 자체는 첫번째 인덱스의 값을 가르킴
            # [1]의 뜻은 변수가 가르키고 있는 곳으로 부터 1번째 칸 
            # [0]은 변수가 가르키고 있는 곳으로부터 0번째 칸
        
        # -1
            # 맨 앞이 0이니까 맨 뒤는 -1,-2,,
        
        # 범위

class_score[0:1]
print(type(class_score[1])) #int
print(type(class_score[0:1])) #list

        # find 시간복잡도 : 최악의 경우 n초(인덱스 순서대로)


## 2.2-1) 다차원 리스트
    # 리스트 안에 리스트
a=[
    1,
    2,
    [3,4]
]

# 2.3) 튜플(tuple)
    #리스트와 달리 () 사용
a=(1,2)
type(a) #tuple

    #리스트와 차이
        # 리스트 : 인덱스의 값을 바꿀 수 있음 (재할당)
        # 튜플   : 인덱스의 값을 바꿀 수 없음, 값의 추가, 삭제 불가
# a[0] =3 


# 2.4) 문자열(String)
b = 'hello world'
print(b)
    
    #문자열의 인덱싱
print(b[2]) #l


## 2.5 ) 딕셔너리(dict)
    #사전의 단어와 뜻이 저장되는 방식과 동일
    # key(단어) : value(뜻)
    # key를 통해 value를 찾음

#dict 선언 1
my_dict = {123: 456,
           "my_key": "hello"}
print(my_dict)

#dict 선언 2
my_dict2 = dict(my_key=456,
                hello=1000)
    #여기서는 key가 무조건 문자열이어야 -> 함수 호출이라서

    #dict가 필요한 이유?
        #dict가 RAM에서 저장되는 방식
            #dict의 사전적 의미는 hash table
                #hash brown 연상 : 믹서기에 갈아서 -> 나온 숫자가 메모리의 '주소(key)'에 '값'을 저장

    # find 시간복잡도 : 1 (해당 key의 값만 찾으면 되므로)


## 2.6) 집합(Set)
c = {1,2,3,1} #1 중복은 1개로 본다.
print(c) #{1, 2, 3}

my_list = {1,2,3,4,4}
print(my_list)
set(my_list) #Set 으로 변경 -> 중복을 제거하고 싶을 때
print(my_list)


## 2.7) Bool, Boolean
d = True
print(True and False) #False
print(True or False) #True
