class Order:

    def __init__(self, ORDERLIST):
        self.ORDERLIST = ORDERLIST

    #1
    def validateOrder(self):
        list1 =[]

        if(self.ORDERLIST.__len__()==0):
            return False
        
        elif(type(self.ORDERLIST)!=type(list1)):
            return False
        
        for menu in self.ORDERLIST:
            if (type(menu[0]) != type("str") or type(menu[1]) != type(1)):
                return False      
        else:
            return True

    #2
    def calcPrice(self):
        totalPrice = 0
        for menu in self.ORDERLIST:
            totalPrice +=menu[1]
        return totalPrice
    
class Restaurant:
    totalOrder = 0 


class NormalRestaurant(Restaurant):
    

    def __init__(self, tableNum):            
        self.tableNum = tableNum        
        self.availableTable = tableNum  
        self.orderlist =[]              
    
    #3
    def makeOrder(self, targetOrder):
        if(Order.validateOrder(targetOrder) == False):
            return False
        
        # 가용 테이블이 없으면
        if(self.availableTable == 0):
            return False

        else:
            self.orderlist.append(targetOrder)
            self.availableTable -=1 # 가용 테이블 -1
            self.totalOrder +=1 # Restaurant에서 관리중인 order 총합 +1
            return True

    #4 가게 내부 테이블 개수 리턴
    def getTotalTables(self):
        return self.tableNum
    
    #5 가용 테이블 개수 리턴
    def getAvailableTables(self):
        return self.availableTable
    
    #6 현재 주문 내역의 개수 
    def getCurrentOrders(self):
        return self.orderlist.__len__()

    #7 
    def clearOrder(self):
        if (self.orderlist.__len__()==0):
            return False
        else:
            totalPrice = 0
            tmp = self.orderlist.pop(0) # list의 맨 앞 주문 빼고
            for menu in tmp:            # 맨 앞 주문에 속한 메뉴들
                totalPrice += menu[1]
            self.availableTable +=1
            return totalPrice
    
    def getTotalOrders(self): 
        return self.totalOrder.__len__()


class DriveThruRestaurant(Restaurant):
    orderList =[]

    #8
    def makeOrder(self, targetOrder):
        if(Order.validateOrder(targetOrder) ==False):
            return False
        else:
            self.orderList.append(targetOrder)
            self.totalOrder +=1 #전체 Restaurant의 주문 개수 +1
            return self.orderList.__len__() # 현재 주문 내역의 개수 리턴
    
    #9
    def clearOrder(self):
        if (self.orderList.__len__()==0):
            return False
        else:
            totalPrice = 0
            tmp = self.orderList.pop(0)
            for menu in tmp:
                totalPrice +=menu[1]
            return totalPrice

    #10    
    def getTotalOrders(self): 
        return self.totalOrder.__len__()



