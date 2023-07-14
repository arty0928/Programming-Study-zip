# ANSWER
# [START]

class Database:
    
    def __init__(self):
        self.customerList = {}

    #1 새로운 dictionary 추가, 추가한 dictionary 반환
    def registNewCustomer(self, customerId, customerName):
        tmp ={}
        for key,value in self.customerList.items():
            #key에 해당하는 value 없으면
            if self.customerList.get(key) == None:
                self.customerList[customerId] = customerName
                tmp[customerId] = customerName
                return tmp
            else:
                return -1

    #2 dictionary에 저장된 key 개수 반환
    def getCustomerNumber(self):
        return len(self.customerList)
    
    #3 key 있는지 확인 후 dictionary 반환return 
    def getCustomerNameByID(self, customerId):
        tmp = {}

        # key 가 dictionary에 존재
        if self.customerList.get(customerId)!=None:
            tmp[customerId] = self.customerList[customerId]
            return tmp
        else:
            return -1
    
    #4# 중복 value들을 dictionary에 저장해서 반환
    def getCustomerIDByName(self,customerName):
        tmp ={}
        count = 0
        for key, value in self.customerList.items(): 
            # 일치하는 value 가 있으면
            if value == customerName:
                # dictionary tmp에 추가
                tmp[key] = customerName
                count +=1
        
        if(count > 0):
            return tmp
        else:
            return -1

    #5
    def getAllCustomer(self):
        return self.customerList
    
    #6 key와 동일한 value 가져오기
    def removeCustomerByID(self, customerId):
        # key에 해당하는 value가 존재하면 
        if self.customerList.get(customerId)!=None:
            # 해당 key,value 삭제 
            self.customerList.pop(customerId)
            return self.customerList
        else:
            return -1
    
    #7 인자와 일치하는 value 모두 삭제
    def removeCustomerByName(self, customerName):
        count = 0
        keys = []
        for key, value in self.customerList.items():
            # 일치하는 key들 keys(리스트) = [dictionary] 형태로 저장
            if value == customerName:
                keys.append(key)
                count +=1
        
        # 일치하는 것이 있으면
        if (count > 0):
            # keys에 있는 key에 해당하는 것들을 내부 dictioanry에서 다 삭제
            for key in keys:
                self.customerList.pop(key)
            return self.customerList
        else:
            return -1

    #8 dictionary value 오름차순 정렬 리스트 
    def getAllCustomerNameSorted(self):
        tmp = []
        for key, value in self.customerList.items():

            # 중복안되게 value 들을 list에 담기
            if (value in tmp) == False:
                tmp.append(value)
        # list 오름차순 정렬
        tmp.sort()
        return tmp

    #9 key들만 오름차순 정렬 리스트
    def getAllCustomerIDSorted(self):
        tmp = []
        for key in self.customerList:
            # if (key in tmp) == False:
                tmp.append(key)
        tmp.sort()
        return tmp

    #10# 모든 중복 value dictionary 반환 
    def getDuplicatedCustomerNames(self):
        names = []
        duplicated_names = []

        for key, value in self.customerList.items():
            # 하나만 있는 value 면 names에 저장
            if (value in names) == False:
                names.append(value)
            
            # 중복 value면 duplicated_names에 저장
            else:
                duplicated_names.append(value)

        tmp = {}

        # 중복 value를 새로운 dictionary tmp에 저장해서 반환
        for key, value in self.customerList.items():
            if value in duplicated_names:
                tmp[key] = value
        return tmp
    

# class Database:

#     def __init__(self):
#         self.db = {}

#     # 1
#     def registNewCustomer(self, customerID, customerName):
#         if self.db.get(customerID) == None:
#             tmp = {}
#             self.db[customerID] = customerName
#             tmp[customerID] = customerName
#             return tmp
#         else:
#             return -1

#     # 2
#     def getCustomerNumber(self):
#         return len(self.db)

#     # 3
#     def getCustomerNameByID(self, customerID):
#         tmp = {}
#         if self.db.get(customerID) != None:
#             tmp[customerID] = self.db[customerID]
#             return tmp
#         else:
#             return -1

#     # 4
#     def getCustomerIDByName(self, customerName):
#         tmp = {}
#         count = 0
#         for key, value in self.db.items():
#             if value == customerName:
#                 tmp[key] = value
#                 count += 1
#         if count > 0:
#             return tmp
#         else:
#             return -1

#     # 5
#     def getAllCustomer(self):
#         return self.db

#     # 6
#     def removeCustomerByID(self, customerID):
#         if self.db.get(customerID) != None:
#             self.db.pop(customerID)
#             return self.db
#         else:
#             return -1

#     # 7
#     def removeCustomerByName(self, customerName):
#         count = 0
#         keys = []
#         for key, value in self.db.items():
#             if value == customerName:
#                 keys.append(key)
#                 count += 1

#         if count != 0:
#             for item in keys:
#                 self.db.pop(item)
#             return self.db
#         else:
#             return -1

#     # 8
#     def getAllCustomerNameSorted(self):
#         tmp = []
#         for key, value in self.db.items():
#             if (value in tmp) == False:
#                 tmp.append(value)
#         tmp.sort()
#         return tmp

#     # 9
#     def getAllCustomerIDSorted(self):
#         tmp = []
#         for key, value in self.db.items():
#             if (key in tmp) == False:
#                 tmp.append(key)
#         tmp.sort()
#         return tmp

#     # 10
#     def getDuplicatedCustomerNames(self):
#         names = []
#         duplicated_names = []

#         for key, value in self.db.items():
#             if (value in names) == False:
#                 names.append(value)
#             else:
#                 duplicated_names.append(value)

#         tmp = {}
#         for key, value in self.db.items():
#             if value in duplicated_names:
#                 tmp[key] = value
#         return tmp

# [END]
# ANSWER

########################################################################
# Scoring
#


score = 0

# problem 1
try:
    myDB = Database()

    solution = [True, True, True]
    answer = []

    res = myDB.registNewCustomer('0001', 'Apple')
    if res == {'0001': 'Apple'}:
        answer.append(True)

    res = myDB.registNewCustomer('0002', 'Tomato')
    if res == {'0002': 'Tomato'}:
        answer.append(True)

    res = myDB.registNewCustomer('0001', 'Apple')
    if res == -1:
        answer.append(True)

    if answer == solution:
        score += 6
        print("[1] SUCCESS")
    else:
        print("[1] FAIL")
except:
    print("[1] FAIL")

# problem 2
try:
    solution = 3
    answer = 0

    myDB = Database()

    myDB.registNewCustomer('0001', 'Apple')
    myDB.registNewCustomer('0002', 'Tomato')
    myDB.registNewCustomer('0009', 'Peach')

    answer = myDB.getCustomerNumber()
    # print(answer)

    if answer == solution:
        score += 6
        print("[2] SUCCESS")
    else:
        print("[2] FAIL")
except:
    print("[2] FAIL")

# problem 3
try:
    solution = {'0002': 'Tomato'}
    answer = 0

    myDB = Database()

    myDB.registNewCustomer('0001', 'Apple')
    myDB.registNewCustomer('0002', 'Tomato')
    myDB.registNewCustomer('0009', 'Peach')

    answer = myDB.getCustomerNameByID('0002')
    # print(answer)

    if answer == solution:
        answer = myDB.getCustomerNameByID('0010')
        if answer == -1:
            score += 6
            print("[3] SUCCESS")
        else:
            print("[3] FAIL")
    else:
        print("[3] FAIL")
except:
    print("[3] FAIL")


# problem 4
try:
    solution = {'0002': 'Tomato', '0004': 'Tomato'}
    answer = 0

    myDB = Database()

    myDB.registNewCustomer('0001', 'Apple')
    myDB.registNewCustomer('0002', 'Tomato')
    myDB.registNewCustomer('0004', 'Tomato')
    myDB.registNewCustomer('0009', 'Peach')

    answer = myDB.getCustomerIDByName('Tomato')
    # print(answer)

    if answer == solution:
        if myDB.getCustomerIDByName('XXX') == -1:
            score += 6
            print("[4] SUCCESS")
        else:
            print("[4] FAIL")
    else:
        print("[4] FAIL")
except:
    print("[4] FAIL")

# problem 5
try:
    solution = {'0001': 'Apple', '0002': 'Tomato',
                '0004': 'Tomato', '0009': 'Peach'}
    answer = 0

    myDB = Database()

    myDB.registNewCustomer('0001', 'Apple')
    myDB.registNewCustomer('0002', 'Tomato')
    myDB.registNewCustomer('0004', 'Tomato')
    myDB.registNewCustomer('0009', 'Peach')

    answer = myDB.getAllCustomer()
    # print(answer)

    if answer == solution:
        score += 6
        print("[5] SUCCESS")
    else:
        print("[5] FAIL")
except:
    print("[5] FAIL")

# problem 6
try:
    solution = {'0001': 'Apple', '0002': 'Tomato',
                '0004': 'Tomato'}
    answer = 0

    myDB = Database()

    myDB.registNewCustomer('0001', 'Apple')
    myDB.registNewCustomer('0002', 'Tomato')
    myDB.registNewCustomer('0004', 'Tomato')
    myDB.registNewCustomer('0009', 'Peach')

    answer = myDB.removeCustomerByID('0009')
    # print(answer)

    if answer == solution:
        if myDB.removeCustomerByID('0009') == -1:
            score += 6
            print("[6] SUCCESS")
        else:
            print("[6] FAIL")
    else:
        print("[6] FAIL")
except:
    print("[6] FAIL")

# problem 7
try:
    solution = {'0001': 'Apple', '0009': 'Peach'}
    answer = 0

    myDB = Database()

    myDB.registNewCustomer('0001', 'Apple')
    myDB.registNewCustomer('0002', 'Tomato')
    myDB.registNewCustomer('0004', 'Tomato')
    myDB.registNewCustomer('0009', 'Peach')

    answer = myDB.removeCustomerByName('Tomato')
    # print(answer)

    if answer == solution:
        if myDB.removeCustomerByName('Tomato') == -1:
            score += 6
            print("[7] SUCCESS")
        else:
            print("[7] FAIL!")
    else:
        print("[7] FAIL!!")
except:
    print("[7] FAIL!!!")

# problem 8
try:
    solution = ['Apple', 'Peach', 'Tomato']
    answer = 0

    myDB = Database()

    myDB.registNewCustomer('0001', 'Apple')
    myDB.registNewCustomer('0002', 'Tomato')
    myDB.registNewCustomer('0004', 'Tomato')
    myDB.registNewCustomer('0009', 'Peach')

    answer = myDB.getAllCustomerNameSorted()
    # print(answer)

    if answer == solution:
        score += 6
        print("[8] SUCCESS")
    else:
        print("[8] FAIL")
except:
    print("[8] FAIL")

# problem 9
try:
    solution = ['0001', '0002', '0004', '0009']
    answer = 0

    myDB = Database()

    myDB.registNewCustomer('0001', 'Apple')
    myDB.registNewCustomer('0009', 'Peach')
    myDB.registNewCustomer('0004', 'Tomato')
    myDB.registNewCustomer('0002', 'Tomato')

    answer = myDB.getAllCustomerIDSorted()
    # print(answer)

    if answer == solution:
        score += 6
        print("[9] SUCCESS")
    else:
        print("[9] FAIL")
except:
    print("[9] FAIL")


# problem 10
try:
    solution = {'0002': 'Tomato', '0004': 'Tomato',
                '0009': 'Peach', '0008': 'Peach'}
    answer = 0

    myDB = Database()

    myDB.registNewCustomer('0001', 'Apple')
    myDB.registNewCustomer('0002', 'Tomato')
    myDB.registNewCustomer('0004', 'Tomato')
    myDB.registNewCustomer('0009', 'Peach')
    myDB.registNewCustomer('0008', 'Peach')

    answer = myDB.getDuplicatedCustomerNames()
    #  print(answer)

    if answer == solution:
        score += 6
        print("[0] SUCCESS")
    else:
        print("[0] FAIL")
except:
    print("[0] FAIL")

print("\nTOTAL SCORE -->> ", score, "\n")


# 채점시 주의사항
# 1) 모든 문제에서 새롭게 Database 객체를 만들어서 사용할 것임
# 2) 모든 문제에서 registNewCustomer()를 사용하여 항목을 추가함. 따라서 메소드가 틀리면 연쇄적으로 오점 처리됨
