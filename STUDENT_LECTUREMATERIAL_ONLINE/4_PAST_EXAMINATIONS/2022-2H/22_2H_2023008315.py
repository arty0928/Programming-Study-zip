class MyClass:

    numberOfObject =0
    
    #1
    def __init__(self,id):
        self.id = id
        MyClass.numberOfObject +=1
        self.dictionary={}
    
    #2
    def getId(self):
        return self.id

    #3
    def setId(self, id):
        if (type(id) == type(1) or type(id) == type(1.0)):
            self.id ="XXXX"
        else:
            self.id = id
    
    #4
    def getNumberOfObject(self):
        return MyClass.numberOfObject
    
    #5
    def storeWordlistAsDictionary(self, my_list):
        my_list.sort()
        for word in my_list:
            if word in self.dictionary:
                self.dictionary[word] +=1
            else:
                self.dictionary[word] = 1
        return self.dictionary
    
    #6
    def getWordCount(self, my_list):
        for key, value in self.dictionary.items():
            if key == my_list:
                tmp = (key, value)
                return tmp
        
        return False
            
    #7
    def getWordList(self):
        if self.dictionary.__len__()==0:
            return False
        else:
            tmp = []
            for key,value in self.dictionary.items():
                tmp.append(key)
                tmp.sort()
            return tmp
    
#8
class MyDerivedClass(MyClass):

    def __init__(self, id="****"):
        super().__init__(id)
    
    #8번
    def __str__(self):
        #비어있다면
        if self.dictionary.__len__()==0:
            return "<>"
        else:
            tmp =[]
            # key 리스트만
            for key, value in self.dictionary.items():
                tmp.append(key)

            result = "<"+",".join(key for key in tmp)+">"
            return result
    
    #9번
    def __gt__(self, target):
        if (self.dictionary.__len__() > target.dictionary.__len__()):
            return True
        else:
            return False
    
    #10
    def __add__(self, target):
        newdict ={}
        for key, value in self.dictionary.items():
            newdict[key]=value

        # target dictionary에서
        for key,value in target.dictionary.items():
            # 내부 dictionary의 key 값과 동일한 것이 있으면
            if key in newdict:
                newdict[key] += value
            # 내부 dictioanry에 없는 새로운 key값이 추가되었으면
            else:
                newdict[key] = value

        # 새로운 객체에 저장하여 기존 객체들의 정보 유지
        newObject = MyDerivedClass()
        newObject.dictionary = newdict
        return newObject 

    

#8번
# tmp = ["문자열0","문자열1","문자열2"]
# result = "<"+",".join(key for key in tmp)+">"
# print(result)







d = {'문자열1':1, "문자열2":2}

if '문자열1' in d:
    print("있음")












# class MyClass:

#     # 생성된 객체의 누적개수
#     numberOfObject = 0

#     #1
#     def __init__(self,id):
#         self.id = id # 객체 내부에서 보관중인 식별자
#         MyClass.numberOfObject +=1
#         self.stored_dictionary={} 

#     #2  객체 내부에서 보관중인 식별자 반환
#     def getId(self):
#         return self.id
    
#     #3 정수 혹은 실수인 경우 식별자 구분해서 저장
#     def setId(self, id):
#         if(type(id)==type(1) or type(id)==type(1.0)):
#             self.id = "XXXX"
#         else:
#             self.id = id
    
#     #4 class를 이용해서 만든 객체의 누적개수 반환
#     def getNumberOfObject(self):
#         return MyClass.numberOfObject
    
#     #5 인자 리스트 정렬 후, self 에 추가
#     def storeWordlistAsDictionary(self,my_list):
#         sorted_list = sorted(my_list)
#         for item in sorted_list:
#             if item in self.stored_dictionary:
#                 self.stored_dictionary[item] +=1
#             else:
#                 self.stored_dictionary[item]=1
#         return self.stored_dictionary

#     #6 key에 해당하는 value가 있으면 튜플 형태로 key, value 반환
#     def getWordCount(self,my_string):
#         if my_string in self.stored_dictionary:
#             return (my_string, self.stored_dictionary[my_string])
#         else:
#             return False

#     #7 dictionary 비어있는지 확인, key값들만 리스트에 저장 후 오름차순 정렬
#     def getWordList(self):
#         if(self.stored_dictionary.__len__()!=0):
#             new_list=[]
#             for key in self.stored_dictionary: #key값들 for문
#                 new_list.append(key)
#             return sorted(new_list)
#         else:
#             return False
    
# class MyDerivedClass(MyClass):

#     def __init__(self,id="****"):
#         # self.id=id
#         super().__init__(id)
    
#     # dictionary 가 비어있지 않으면 출력 형태를 변경해서 모든 key들 반환
#     def __str__(self):
#         if(len(self.stored_dictionary)==0):
#             return "<>"
#         else:
#             new_list = []
#             for key in self.stored_dictionary: #key
#                 new_list.append(key)
#             formatted_list = "<"+",".join(str(key) for key in new_list)+">" 
#             return formatted_list

#     # 보다 큰 수 (다른 객체와 비교)
#     def __gt__(self, other):
#         if(len(self.stored_dictionary) > len(other.stored_dictionary)):
#             return True
#         else:
#             return False
    
#     #10 + 연산, 새로운 객체 생성해서 반환
#     def __add__(self, other):
#         newDictionary={}
#         for key,value in self.stored_dictionary.items():
#             newDictionary[key] = value

#         for key, value in other.stored_dictionary.items():
#             # target의 key가 내부 dictionary에 있다면
#             if key in self.stored_dictionary:
#                 newDictionary[key] += value
#             else:
#                 newDictionary[key] = value
#         newObject = MyDerivedClass()
#         newObject.stored_dictionary = newDictionary
#         return newObject


# # dictionary = {'name':1, 'apple':2}
# # new_list=[]
# # for name in dictionary.keys():
# #     new_list.append(name)
# # formatted_list = "<"+",".join(str(key) for key in new_list)+">"
# # print(formatted_list)


# # 리스트를 괄호없이 원하는 형태로 반환
# # my_list = [1, 2, 3]
# # formatted_list = "<" + ", ".join(str(x) for x in my_list) + ">"
# # print(formatted_list)
# # # 출력: <1, 2, 3>

# dictionary = {'name':1, 'apple':2}
# for item in dictionary:
#     print(item)

# new=[]
# for key in dictionary.keys():
#     new.append(key)
# print(sorted(new))