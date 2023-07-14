from datetime import datetime

def makeRecord(personName, deadline, todoNum, priarty):
    #담당자 이름 문자열
    #종료기한 20000928
    #수행항목번호 A001
    #우선순위 1 2 3 중 하나
    if(len(todoNum)==4):
        if(type(todoNum)==str):
            todolist = [personName, deadline, todoNum, priarty]

    return todolist

def checkDeadline(inserted_list, today):
    # current_time = str(datetime.now()) #2021-01-02 22:41:10.181418
    # current = current_time.split(" ")[0].replace("-","") #20230709

    if(inserted_list[1].startswith("2020")==False):
        return False
    elif(inserted_list[1][4:6]>12 or inserted_list[1][4:6]<1):
        return False
    elif(inserted_list[1][6:]>31 or inserted_list[1][6:]<1):
        return False
    elif(inserted_list[1]-today <0):
        return False
    return True

def checkPriority(inserted_list):
    if(inserted_list[3] in [1,2,3]):
        return True
    return False


class ToDoList:
    #담당자 이름
    #종료기한
    #수행항목번호
    #우선순위
    todolist =[]

    #초기화
    def __init__(self):
        self.todolist = []


    def checkDeadline(self,deadline):
        if(len(deadline)!=8):
            return -1
        else:
            return 1

    
    def checkPriority(self,priority):
        if(priority not in [1,2,3]):
            return -1
        return 1
    
    def checkTodoNumIsAdded(self,todoNum):
        for i in len(self.todolist):
            if(todoNum == i.todoNum):
                return -1   
        return 1


    def addItem(self, insertinglist):
        checkDeadline = checkDeadline(insertinglist.deadline)
        checkPriority = checkPriority(insertinglist.priority)
        if(checkDeadline!=-1 and checkPriority !=-1):
            checkTodoNumIsAdded = checkTodoNumIsAdded(insertinglist.todoNum)
            if(checkTodoNumIsAdded!=-1):
                self.todolist.append(insertinglist)       
                return len(self.todolist)
        return False

    def getEarliestItem(self):
        sortedList =[]

        for i in self.todolist:
            current_time = str(datetime.now()) #2021-01-02 22:41:10.181418
            current = current_time.split(" ")[0].replace("-","") #20230709
            date = i - current

            sortedList = sorted(self.todolist, key = (date, i[3], self.todolist.index(i)))
        
        return sortedList[0]
            
        
    def getItemByName(self,personName):
        new_list=[]
        if(self.todolist.__contains__(personName)):
            for i in self.todolist:
                if(i[0]==personName):
                    new_list.append(i)
            sorted_list = sorted(new_list, key=lambda x: (x[1], x[3], self.todolist.index(x)))
            return sorted_list
        else:
            return False

    def getItemsByEDF(self,option): #option: bool
        bigList=[]
        bigList = sorted(self.todolist, key=lambda x: (x[1], x[3], self.todolist.index(x)))
        
        if(option==False):
            return bigList.reverse()
        return bigList

    
    def getItemDeadline(self,todoNum):
        if(self.todolist.__contains__(todoNum)==False):
            # list에서 x를 포함하는 index return : my_list.index(x)
            return False
        else: 
            return True

    def deferDeadline(self, todoNum, delayedDate):
        index = self.todolist.index(todoNum)
        if(index):
            self.todolist[index][1] = self.todolist[index][1] + delayedDate
            if(self.todolist[index][1][6:]>31):
                self.todolist[index][1][6:] = self.todolist[index][1][6:] - 31
                self.todolist[index][1][4:6] = self.todolist[index][1][4:6] + 1

                if(self.todolist[index][1][4:6] >= 13):
                    self.todolist[index][1][4:6] = self.todolist[index][1][4:6] - 12
                    self.todolist[index][1][0:4] = self.todolist[index][1][0:4] + 1

            return self.todolist[index][1]

        else:
            return False      
    

    def writeFile(self):
        output_file = open('output.csv')
        writeList = self.getItemsByEDF(True)
        for i in writeList:
            new_line = '{0},{1},{2},{3}'.format(i[0],i[1],i[2],i[3])
            output_file.write(new_line)
        