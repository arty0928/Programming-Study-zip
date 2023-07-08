# file을 처음 open하면 file cursor가 맨 앞줄에 위치
# file = open('STUDENT_LECTUREMATERIAL_ONLINE\\2_PRACTICE\\Practice_13_File\\fileexamples\\file_example.txt','r')
# contents = file.read()
# print(contents) 
# file.close() #open한 file은 반드시 close 해야 함 




#error 확인 후 진행
# with -> error 확인, 끝나면 자동 close
# with open('STUDENT_LECTUREMATERIAL_ONLINE\\2_PRACTICE\\Practice_13_File\\fileexamples\\file_example.txt','r') as file:

# with open('STUDENT_LECTUREMATERIAL_ONLINE\\2_PRACTICE\\Practice_13_File\\fileexamples\\file_example.txt','r') as file:
#     contents = file.read()

# print(contents) 




# with open('STUDENT_LECTUREMATERIAL_ONLINE\\2_PRACTICE\\Practice_13_File\\fileexamples\\file_example.txt','r') as file:
#     # 한줄씩(한줄에 하나씩)
#     contents = file.readlines()

# for p in contents:
#     print(p.strip())



## for line in file (줄의 글자수)
file = open('STUDENT_LECTUREMATERIAL_ONLINE\\2_PRACTICE\\Practice_13_File\\fileexamples\\file_example.txt','r')
for line in file:
    # print(len(line))
    print(len(line.strip()))
file.close()


