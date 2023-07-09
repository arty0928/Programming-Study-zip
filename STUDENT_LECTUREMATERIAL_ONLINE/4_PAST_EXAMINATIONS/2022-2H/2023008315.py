class MyClass:

    numberOfObject = 0

    def __init__(self,id):
        self.id = id
        MyClass.numberOfObject +=1
        self.stored_dictionary={}


    def getId(self):
        return self.id
    
    def setId(self, id):
        if(type(id)==int or type(id)==float):
            self.id = "XXXX"
        else:
            self.id = id
    
    def getNumberOfObject(self):
        return MyClass.numberOfObject
    
    def storeWordlistAsDictionary(self,my_list):
        sorted_list = sorted(my_list)
        for item in sorted_list:
            if item in self.stored_dictionary:
                self.stored_dictionary[item] +=1
            else:
                self.stored_dictionary[item]=1
        return self.stored_dictionary

    def getWordCount(self,my_string):
        if my_string in self.stored_dictionary:
            return (my_string, self.stored_dictionary[my_string])
        else:
            return False

    def getWordList(self):
        if(self.stored_dictionary.__len__!=0):
            new_list=[]
            for key in (self.stored_dictionary.keys()):
                new_list.append(key)
            return new_list
        else:
            return False
    
class MyDerivedClass(MyClass):

    def __init__(self,id="****"):
        # self.id=id
        super().__init__(id)
        
    def __str__(self):
        if(len(self.stored_dictionary)==0):
            return "<>"
        else:
            new_list = []
            for key in self.stored_dictionary.keys():
                new_list.append(key)
            formatted_list = "<"+",".join(str(key) for key in new_list)+">" 
            return formatted_list

    def __gt__(self, other):
        if(len(self.stored_dictionary) > len(other.stored_dictionary)):
            return True
        else:
            return False
    
    def __add__(self, other):
        newDictionary = MyClass()
        for key in self.stored_dictionary:
            if(other.stored_dictionary.__contains__(key)):
                newDictionary.stored_dictionary[key] = self.stored_dictionary[key] + other.stored_dictionary[key]
        
        return newDictionary



# dictionary = {'name':1, 'apple':2}
# new_list=[]
# for name in dictionary.keys():
#     new_list.append(name)
# formatted_list = "<"+",".join(str(key) for key in new_list)+">"
# print(formatted_list)


# 리스트를 괄호없이 원하는 형태로 반환
# my_list = [1, 2, 3]
# formatted_list = "<" + ", ".join(str(x) for x in my_list) + ">"
# print(formatted_list)
# # 출력: <1, 2, 3>

dictionary = {'name':1, 'apple':2}
for item in dictionary:
    print(item)

new=[]
for key in dictionary.keys():
    new.append(key)
print(sorted(new))