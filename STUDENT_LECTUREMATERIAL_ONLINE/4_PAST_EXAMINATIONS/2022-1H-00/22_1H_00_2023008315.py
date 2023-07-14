class Database:
    
    def __init__(self):
        self.customerList = {}

    #1 새로운 dictionary 추가, 추가한 dictionary 반환
    def registNewCustomer(self, customerId, customerName):
        tmp ={}
        for key,value in self.customerList.items():
            if self.customerList.get(key) == None:
                self.customerList[customerId] = customerName
                tmp[customerId] = customerName
                return tmp
            else:
                return -1
    #2
    def getCustomerNumber(self):
        return len(self.customerList)
    
    #3 key 있는지 확인 후 dictionary 반환return 
    def getCustomerNameByID(self, customerId):
        tmp = {}
        if self.customerList.get(customerId)!=None:
            tmp[customerId] = self.customerList[customerId]
            return tmp
        else:
            return -1
    
    #4
    def getCustomerIDByName(self,customerName):
        tmp ={}
        count = 0
        for key, value in self.customerList.items(): 
            if value == customerName:
                tmp[key] = customerName
                count +=1
        
        if(count > 0):
            return tmp
        else:
            return -1

    #5
    def getAllCustomer(self):
        return self.customerList
    
    #6
    def removeCustomerByID(self, customerId):
        if self.customerList.get(customerId)!=None:
            self.customerList.pop(customerId)
            return self.customerList
        else:
            return -1
        # for customer in self.customerList: #key
        #     if customer == customerId: #key
        #         self.customerList.pop(customer)
        #         return self.customerList
        # return -1

    #7 인자와 일치하는 value 모두 삭제
    def removeCustomerByName(self, customerName):
        count = 0
        keys = []
        for key, value in self.customerList.items():
            if value == customerName:
                keys.append(key)
                count +=1
        
        if (count > 0):
            for key in keys:
                self.customerList.pop(key)
            return self.customerList
        else:
            return -1

    #8
    def getAllCustomerNameSorted(self):
        tmp = []
        for key, value in self.customerList.items():
            if value in tmp == False:
                tmp.append(value)
            tmp.sort()
            return tmp
    
        
    #9 key 오름차순 정렬 리스트
    def getAllCusotmerIDSorted(self):
        idList =[]

        for id in self.customerList:
            # if key in idList == False:
                idList.append(id)

        idList.sort()
        return idList

    #10 모든 중복 value dictionary 반환 
    def getDuplicatedCustomerNames(self):
        names =[]
        duplicated_names=[]

        for key, value in self.customerList.items():
            if (value in names) == False:
                names.append(value)
            else:
                duplicated_names.append(value)
            
        tmp = {}
        for key,value in self.customerList.items():
            if value in duplicated_names:
                tmp[key] = value
        
        return tmp

    


d = {'1':'jenny', '2':'anna','3':'anna','4':'anna'}
duplicated ={}
for key, value in d.items(): #기준
    for k, v in d.items():
        if key == k:
            # print(key,k)
            # print("break")
            break
        if d[key]==d[k]:
            duplicated[key] = d[key]
print(duplicated)
# duplicatedList = {}
# for i in d:
#     for j in d:
#         if d[i] == d[j]:
#             duplicatedList[i] = d[j]

# print(duplicatedList)
# names = set()
# for i in d.items:
#     print(i)

# namesList =[]
# for name in names:
#     namesList.append(name)

# namesList.sort()
# print(namesList)

# for num in d.values:
    # print(num) 
    # if '1' == num:
        # d.pop(num) 
        # print(d)
         
# for cusotmer in d:
#     print(d[cusotmer])

# d['3']='joy'
# print(d)

# print(len(d))
