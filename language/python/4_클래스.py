## 4.1) 클래스(class) = 규약
    # 집을 만들때 필요한 건?
        #설계도를 통해 다양한 형태로 집을 만들 수 있다.(기본 특성이나 성질은 클래스라는 규약으로 정의)
        #클래스를 통해 만든 것을 객체(object)

        #사용자가 직접 클래스를 정의할 수 있다 
            # 붕어빵 틀(설계도) -> new 붕어빵(객체 object)
                # 형태는 붕어빵이지만 각각의 내부는 마음대로 정의

#class 클래스이름:
    # 명사(attribute) 초기화
    # 동사(behavior) 정의

#  파이썬 클래스는 맨앞은 무조건 대문자 + 카멜 케이스
class SoccerPlayer:
    # 인자가 2개면 self 포함 3개를 넣어야 함
    # self는 클래스 내부에서 정의되므로 무조건 포함해야 함(인자를 넣을 때는)
    def shoot(self,x,y):
        print("슛을 날립니다.")
        print("슈윳")
    
    #def pass() -> pass()는 파이썬 문법이라서 오류가 남
    def pass_the_ball(self):
        print("패스를 합니다.")

player = SoccerPlayer() #SoccerPlayer라는 틀에 찍어내서 나온 모양에 player라는 이름을 붙여줌
#SoccerPlayer의 주솟값을 가리키는 애가 player

#객체에 대해서 슛을 날림
player.shoot()
player.pass_the_ball()

player1 = SoccerPlayer() #SoccerPlayer라는 틀에 찍어내서 나온 모양에 player1라는 이름을 붙여줌
player2 = SoccerPlayer() #SoccerPlayer라는 틀에 찍어내서 나온 모양에 player2라는 이름을 붙여줌

player1.shoot()
player2.shoot()


## 1.4.1.2  attribute 초기화
class SoccerPlayer:
    def __init__(self): #생성자, 언더바로 시작하여 원래 init의 기능을 이것으로 대체하겠다 (overriding)
        print("나 태어났어")
    def shoot(self):
        print("슛을 때립니다")

player1 = SoccerPlayer() #SoccerPlayer를 호출하면서 init으로 생성자 실행   player1가 생성되기 전에 print가 출력 

SoccerPlayer.__init__()

####

class SoccerPlayer:
    def __init__(self, height, weight): #생성자, 언더바로 시작하여 원래 init의 기능을 이것으로 대체하겠다 (overriding)
        print("나 태어났어")
        self.wow_height = height
        self.wow_weight = weight

    def shoot(self):
        print("슛을 때립니다")

player1 = SoccerPlayer(height = 180, weight = 50)
player2 = SoccerPlayer(height = 160, weight = 70)

print(player1.wow_height)
print(player1.wow_weight)

print(player2.wow_height)
print(player2.wow_weight)
#설계도는 같지만 창문이나 인테리어를 다르게 하는 것처럼 player1과 player2는 다른것, 각 객체로 존재


####
class SoccerPlayer:
    def __init__(self, height, weight): #생성자, 언더바로 시작하여 원래 init의 기능을 이것으로 대체하겠다 (overriding)
        print("나 태어났어")
        self.wow_height = height
        self.wow_weight = weight

    def shoot(self):
        self.wow_height = self.wow_height + 1
        print("슛을 때립니다")

player1 = SoccerPlayer(180,70)
player1.wow_height  #180
player1.shoot() #wow_height = 181

player2 = SoccerPlayer(160,50)
player2.wow_height  #160
player2.shoot() #wow_height = 161
player1.wow_height  #181


## 1.4.2 상속(inheritance)
class Human:
    def __init__(self, wow_weight, wow_height):
        self.weight = wow_weight
        self.height = wow_height

    def walk(self):
        print("걷습니다")

h1= Human(50,170)
h1.walk()

#Human을 Athelete에 상속하기
class Athelete(Human):
    #Human을 상속함으로써 아래 내용이 포함됨    
    # def __init__(self, wow_weight, wow_height):
    #     self.weight = wow_weight
    #     self.height = wow_height

    # def walk(self):
    #     print("걷습니다")

    def workout(self):
        print("운동을 합니다")

h2 =Athelete(50,180)
h2.walk()


class Athelete(Human):
    #Human에 내용 추가를 하고 싶으면
    def __init__(self, wow_weight, wow_height, fat_rate): #생성자
        super().__init__(wow_weight, wow_height)  #이거는 부모의 내용을 그대로
        self.fat_rate = fat_rate

    def workout(self):
        print("운동을 합니다")


# 상속을 여러번

class SoccerPlayer(Athelete):

    # 부모의 workout과는 다름 -> 부모의 내용을 덮어쓰기(overwrite)
    def workout(self):
        print("축구를 한다")
    
h4 = SoccerPlayer(50,180,50)
h4.walk()
h4.workout() #축구를 한다

# 상속은 원래 object를 자동적으로 상속받음 -> __init__ 형태로 생성자를 만들어야하는 이유도 규약임.
class Human(object):
    def __init__(self, wow_weight, wow_height):
        self.weight = wow_weight
        self.height = wow_height

    def walk(self):
        print("걷습니다")


### 1.4.3) 파이썬 기본 자료형(클래스)별 api 살펴보기
# api(application programming interface)
    # 프로그래밍 언어, 라이브러리, 어플리케이션 등이 제공하는 기능들을 제어할 수 있게 만든 인터페이스
a=[1,2,3]
a.append(3)

c={"c":123}
c.keys()

### 1.4.4) 객체를 인스터스 변수로 가지고 있기

# team = Team(
#     coach, 
#     palyer_list = [
#         player1, 
#         player2, 
#         player3
#     ]
# )

### 1.4.5) 객체 method의 cascading

team = Team(
    coach, 
    palyer_list = [
        SoccerPlayer(70), 
        SoccerPlayer(80), 
    ]
)

team.player_list[0].walk()
# cascading : 앞에서부터 실행, 객체를 부르고 부르고 



