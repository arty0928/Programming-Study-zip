# ANSWER
# [START]
## List 이용한 문제

class Server:

    def __init__(self):
        self.orderedList =[] #["주문번호",['잡채','떡볶이']]

    #1 새로운 주문 리스트에 추가
    def makeOrder(self, orderNum, orderList):
        for order in self.orderedList:
            if (orderNum == order[0]):
                return -1
        tmp = [orderNum, orderList]
        self.orderedList.append(tmp)
        return tmp
    
    #2# 리스트에 있는 주문 길이 만큼 소요시간 측정
    def getWaitingTime(self, orderNum, timePerOrder):
        isExisted = False
        totalTime =0 # 소요시간
        
        for order in self.orderedList:
            if orderNum == order[0]:
                isExisted = True
                index = self.orderedList.index(order)
        
        if(isExisted==True):
            for order in self.orderedList[:index+1]:
                totalTime += len(order[1]) * timePerOrder
            return totalTime            
        else:
            return -1

    #3 list 마지막 인덱스 pop 삭제
    def serveOrder(self):
        tmp = self.orderedList.pop(0)
        return (tmp[0],tmp[1])
    
    #4 리스트 길이 
    def getOrderNumber(self):
        return len(self.orderedList)
    
    #5 리스트 찾아서 삭제 후 반환
    def cancelOrder(self, orderNum):
        for order in self.orderedList:
            if orderNum == order[0]:
                index = self.orderedList.index(order)
                tmp = self.orderedList.pop(index)
                return tmp
        return (-1,-1)

    #6 리스트 중에서 찾아서 리스트 맨 앞으로 옮기기
    #   주문 번호들만 리스트로 반환
    def makeOrderVIP(self, orderNum, orderList):
        for order in self.orderedList:
            if orderNum == order[0]:
                return (-1,-1)

        orderNumList =[]
        tmp = [orderNum, orderList]
        self.orderedList.insert(0,tmp)
        for i in self.orderedList:
            orderNumList.append(i[0])
        return orderNumList

    
    #7 리스트에 존재하는 리스트 찾아서 맨 뒤에 추가
    def giveService(self, orderNum, serviceList):
        for order in self.orderedList:
            if orderNum == order[0]:
                index = self.orderedList.index(order)
                self.orderedList[index][1].append(serviceList)
                return (order[0], order[1])
        return (-1,-1)
    
    # 리스트 속 주문 개수
    def getOrderItems(self):
        tmpOrderNumber = 0 
        for orders in self.orderedList:
            tmpOrderNumber += len(orders[1])
        return tmpOrderNumber
    
# class Server:

#     def __init__(self):
#         self.q = []

#     # 1
#     def makeOrder(self, orderNumber, orderList):
#         existAlready = False
#         for order in self.q:
#             if order[0] == orderNumber:
#                 existAlready = True
#         if existAlready == True:
#             return -1
#         else:
#             tmp = []
#             tmp.append(orderNumber)
#             tmp.append(orderList)
#             self.q.append(tmp)
#             return tmp

#     # 2
#     def getWaitingTime(self, orderNumber, timePerProduct):
#         waitingTime = 0
#         existFlag = False
#         for order in self.q:
#             waitingTime += len(order[1]) * timePerProduct
#             if order[0] == orderNumber:
#                 existFlag = True
#                 break
#         if existFlag == True:
#             return waitingTime
#         else:
#             return -1

#     # 3
#     def serveOrder(self):
#         orderNumber = self.q[0][0]
#         orderList = self.q[0][1]
#         del self.q[0]
#         return orderNumber, orderList

#     # 4
#     def getOrderNumber(self):
#         return len(self.q)

#     # 5
#     def cancelOrder(self, orderNumber):
#         orderIndex = -1
#         count = 0
#         for order in self.q:
#             if order[0] == orderNumber:
#                 orderIndex = count
#                 break
#             count += 1
#         if orderIndex == -1:
#             return -1, -1
#         else:
#             orderNumber = self.q[orderIndex][0]
#             orderList = self.q[orderIndex][1]
#             del self.q[orderIndex]
#             return orderNumber, orderList

#     # 6
#     def makeOrderVIP(self, orderNumber, orderList):
#         existAlready = False
#         for order in self.q:
#             if order[0] == orderNumber:
#                 existAlready = True
#         if existAlready == True:
#             return -1
#         else:
#             tmp = []
#             tmp.append(orderNumber)
#             tmp.append(orderList)
#             self.q.insert(0, tmp)

#             tmp = []
#             for item in self.q:
#                 tmp.append(item[0])
#             return tmp

#     # 7
#     def giveService(self, orderNumber, serviceProduct):
#         orderIndex = -1
#         count = 0
#         for order in self.q:
#             if order[0] == orderNumber:
#                 orderIndex = count
#                 break
#             count += 1
#         if orderIndex == -1:
#             return -1, -1
#         else:
#             orderNumber = self.q[orderIndex][0]
#             self.q[orderIndex][1].append(serviceProduct)
#             orderList = self.q[orderIndex][1]
#             return orderNumber, orderList

#     # 8
#     def getOrderItems(self):
#         count = 0
#         for order in self.q:
#             count += len(order[1])
#         return count

# [END]
# ANSWER

########################################################################
# Scoring
#
score = 0

# 1
try:
    solution = ['0001', ['pizza', 'pie']]
    answer = []

    s = Server()
    answer = s.makeOrder('0001', ['pizza', 'pie'])
    if answer == solution:
        answer = s.makeOrder('0001', ['pizza', 'pie'])
        if answer == -1:
            score += 8
            print("[1] SUCCESS")
        else:
            print("[1] FAIL.a")
    else:
        print("[1] FAIL.b")
except:
    print("[1] FAIL.e")

# 2
try:
    solution = 60
    answer = 0

    score_2 = 0

    s = Server()
    s.makeOrder('0001', ['pizza', 'pie'])
    s.makeOrder('0002', ['pizza', 'pie', 'pasta'])
    s.makeOrder('0003', ['pizza'])

    try:
        answer = s.getWaitingTime('0003', 10)
        if answer == solution:
            answer = s.getWaitingTime('0004', 10)
            if answer == -1:
                score += 8
                score_2 += 8
                print("[2] SUCCESS")
            else:
                print("[2] FAIL.a")
        else:
            print("[2] FAIL.b")
    except:
        print("[2] int error")
        pass

    try:
        if score_2 != 8:
            answer = s.getWaitingTime('0003', '10')
            if answer == solution:
                answer = s.getWaitingTime('0004', '10')
                if answer == -1:
                    score += 8
                    score_2 += 8
                    print("[2s] SUCCESS")
                else:
                    print("[2s] FAIL.a")
            else:
                print("[2s] FAIL.b")
    except:
        print("[2s] string error")
        pass

    if score_2 == 16:
        score -= 8

except:
    print("[2] FAIL.e")

# 3
try:
    solution1 = ['0001', ['pizza', 'pie']]
    solution2 = ['0002', ['pizza', 'pie', 'pasta']]
    answer = 0

    s = Server()
    s.makeOrder('0001', ['pizza', 'pie'])
    s.makeOrder('0002', ['pizza', 'pie', 'pasta'])
    s.makeOrder('0003', ['pizza'])

    num, list = s.serveOrder()

    if num == solution1[0] and list == solution1[1]:
        num, list = s.serveOrder()
        if num == solution2[0] and list == solution2[1]:
            score += 8
            print("[3] SUCCESS")
        else:
            print("[3] FAIL.a")
    else:
        print("[3] FAIL.b")
except:
    print("[3] FAIL.e")

# 4
try:
    solution = [1, 2, 3]
    answer = []

    s = Server()
    s.makeOrder('0001', ['pizza', 'pie'])
    answer.append(s.getOrderNumber())
    s.makeOrder('0002', ['pizza', 'pie', 'pasta'])
    answer.append(s.getOrderNumber())
    s.makeOrder('0003', ['pizza'])
    answer.append(s.getOrderNumber())

    if answer == solution:
        score += 4
        print("[4] SUCCESS")
    else:
        print("[4] FAIL.a")
except:
    print("[4] FAIL.e")

# 5
try:
    solution1 = ['0001', ['pizza', 'pie']]
    solution2 = ['0002', ['pizza', 'pie', 'pasta']]
    answer = 0

    s = Server()
    s.makeOrder('0001', ['pizza', 'pie'])
    s.makeOrder('0002', ['pizza', 'pie', 'pasta'])
    s.makeOrder('0003', ['pizza'])

    num, list = s.cancelOrder('0001')

    if num == solution1[0] and list == solution1[1]:
        num, list = s.cancelOrder('0002')
        if num == solution2[0] and list == solution2[1]:
            res1, res2 = s.cancelOrder('0009')
            if res1 == -1 and res2 == -1:
                score += 8
                print("[5] SUCCESS")
            else:
                print("[5] FAIL.a")
        else:
            print("[5] FAIL.b")
    else:
        print("[5] FAIL.c")
except:
    print("[5] FAIL.e")


# 6
try:
    solution = ['0004', '0001', '0002', '0003']
    answer = 0

    s = Server()
    s.makeOrder('0001', ['pizza', 'pie'])
    s.makeOrder('0002', ['pizza', 'pie', 'pasta'])
    s.makeOrder('0003', ['pizza'])

    answer = s.makeOrderVIP('0004', ['pizza'])

    if answer == solution:
        score += 8
        print("[6] SUCCESS")
    else:
        print("[6] FAIL.a")
except:
    print("[6] FAIL.e")


# 7
try:
    solution = ['0002', ['pizza', 'pie', 'pasta', 'coke']]
    answer = 0

    s = Server()
    s.makeOrder('0001', ['pizza', 'pie'])
    s.makeOrder('0002', ['pizza', 'pie', 'pasta'])
    s.makeOrder('0003', ['pizza'])

    num, list = s.giveService('0002', 'coke')

    if num == solution[0] and list == solution[1]:
        res = s.giveService('0004', 'coke')
        if res1 == -1 and res2 == -1:
            score += 8
            print("[7] SUCCESS")
        else:
            print("[7] FAIL.a")
    else:
        print("[7] FAIL.b")
except:
    print("[7] FAIL.e")

# 8
try:
    solution = 6
    answer = 0

    s = Server()
    s.makeOrder('0001', ['pizza', 'pie'])
    s.makeOrder('0002', ['pizza', 'pie', 'pasta'])
    s.makeOrder('0003', ['pizza'])

    answer = s.getOrderItems()

    if answer == solution:
        score += 8
        print("[8] SUCCESS")
    else:
        print("[8] FAIL.a")
except:
    print("[8] FAIL.e")


print("\nTOTAL SCORE -->> ", score, "\n")

# 채점시 주의사항
# 0) 입장한 순서대로 서비스 하는 구조
# 1) 모든 문제에서 새롭게 Database 객체를 만들어서 사용할 것임
# 2) 모든 문제에서 makeOrder()를 사용하여 주문을 생성함. 따라서 메소드가 틀리면 연쇄적으로 오점 처리됨
