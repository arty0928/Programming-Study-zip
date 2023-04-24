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
