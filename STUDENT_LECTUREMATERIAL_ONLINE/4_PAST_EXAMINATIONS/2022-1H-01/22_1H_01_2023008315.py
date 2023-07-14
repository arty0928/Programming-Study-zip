class Server:

    def __init__(self):
        self.orderedList=[]
    
    #1
    def makeOrder(self, orderNum, orderList):
        for order in self.orderedList:
            if (orderNum == order[0]):
                return -1
        tmp = [orderNum, orderList]
        self.orderedList.append(tmp)
        return tmp
    
    #2
    def getWaitingTime(self, orderNum, timePerOrder):
        totalTime = 0
        for order in self.orderedList:
            # 주문리스트에 있는 경우
            if (orderNum == order[0]):
                index = self.orderedList.index(order)
                for i in self.orderedList[:index+1]:
                    totalTime += len(i[1])

                return totalTime*timePerOrder
        return -1

    #3
    def serveOrder(self):
        tmp = self.orderedList.pop(0)
        return (tmp[0], tmp[1])
    
    #4
    def getOrderNumber(self):
        return len(self.orderedList)

    #5
    def cancelOrder(self, orderNum):
        for order in self.orderedList:
            if (orderNum == order[0]):
                index = self.orderedList.index(order)
                tmp = self.orderedList.pop(index)
                return tmp      
        return (-1, -1)
    
    #6
    def makeOrderVIP(self, orderNum, orderList):
        for order in self.orderedList:
            if (orderNum == order[0]):
                return (-1,-1)
        
        orderNumList =[]
        tmp = [orderNum, orderList]
        self.orderedList.insert(0,tmp)
        for i in self.orderedList:
            orderNumList.append(i[0])
        return orderNumList
    
    #7
    def giveService(self, orderNum, orderList):
        for order in self.orderedList:
            if (orderNum == order[0]):
                index = self.orderedList.index(order)
                self.orderedList[index][1].append(orderList)
                return (self.orderedList[index][0], self.orderedList[index][1])
        return (-1,-1)   
    
    #8
    def getOrderItems(self):
        totalOrderNum =0
        for order in self.orderedList:
            totalOrderNum += len(order[1])
        return totalOrderNum


d=[
    ['1',['우동','라면'] ],
    ['2',['쫄면']],
    ['3',['사리']],
    
]

# 3번
# t=0
# for order in d:
#     if ('2'==order[0]):
#         index = d.index(order)
#         for i in d[:index+1]:
#             t += len(i[1])

# print(t *10)

#8번
# t=0
# for order in d:
#     t += len(order[1])
# print(t)

#7번
# for order in d:
#     if ('3'==order[0]):
#         index=d.index(order)
#         d[index][1].append('서비스')
#         print(d[index][0], d[index][1])

#6번
# tmp = d.pop(1)
# d.insert(0,tmp)
# print(d)

#5번
# for order in d:
#     if '3' == order[0]:
#         index = d.index(order)
#         tmp = d.pop(index)
#         print(tmp)
# print(d)
#4번
t =0
for order in d:
    t += len(order[1])
print(t)

#3번 
# tmp = d.pop()
# print(tmp[0], tmp[1])
        

# 1번 makeOrder
# for order in d:
#     if '1' == order[0]:
#         print('이미 있음')
# tmp = ['2',['라면']]
# d.append(tmp)
# print(d)
# print(tmp)























# class Server:

#     def __init__(self):
#         self.orderedList =[] #["주문번호",['잡채','떡볶이']]

#     def makeOrder(self, orderNum, orderList):
#         for order in self.orderedList:
#             if orderNum == order[0]:
#                 return -1
#         else:
#             self.orderedList.append([orderNum, orderList])
#             return [orderNum,orderList]
    
#     def getWaitingTime(self, orderNum, timePerOrder):
#         isExisted = False
#         for order in self.orderedList:
#             if orderNum == order[0]:
#                 isExisted = True
#                 requiredTime =0 # 소요시간
#                 orderNumIndex = self.orderedList.index(order)
        
#         if(isExisted==True):
#             for order in self.orderedList[:orderNumIndex+1]:
#                 requiredTime += len(order[1]) * timePerOrder
#             return requiredTime            
#         else:
#             return -1

#     def serveOrder(self):
#         removedOrder = self.orderedList.pop(0)
#         return (removedOrder[0],removedOrder[1])
    
#     def getOrderNumber(self):
#         return len(self.orderedList)
    
#     def cancelOrder(self, orderNum):
#         for order in self.orderedList:
#             if orderNum == order[0]:
#                 index = self.orderedList.index(order)
#                 cancelOrder = self.orderedList.pop(index)
#                 return (cancelOrder[0], cancelOrder[1])
#         return (-1,-1)

#     #6
#     def makeOrderVIP(self, orderNum, orderList):
#         for order in self.orderedList:
#             if orderNum == order[0]:
#                 return (-1,-1)
            
#         self.orderedList.insert(0,[orderNum, orderList])
#         orderNumberList =[]
#         for order in self.orderedList:
#             orderNumberList.append(order[0])
#         return orderNumberList
    
#     #7
#     def giveService(self, orderNum, serviceList):
#         for order in self.orderedList:
#             if orderNum == order[0]:
#                 index = self.orderedList.index(order)
#                 self.orderedList[index][1].append(serviceList)
#                 return (order[index][0], order[index][1])
#         return (-1,-1)
    
#     #8
#     def getOrderItems(self):
#         count = 0 
#         for orders in self.orderedList:
#             count += len(orders[1])
#         return count
    


# d=[ ['1',['핫도그','김밥']],
#     ['2',['라면', '감자']]
# ]
# if 1 in d:
#     print("있음") # 안나옴

# print("==append==")
# d[1][1].append('순대')
# print(d[1][0],d[1][1])

# print("==pop==")
# removed = d.pop(0)
# print(removed[0], removed[1])
# print(d)

# print("==insert==")
# d.insert(0,['0',['순대']])
# print(d)

# for order in d:
#     if '1' == order[0]:
#         index = d.index(order)
#         d[index][1].append('쫄면')
#         print(d[index][0], d[index][1])