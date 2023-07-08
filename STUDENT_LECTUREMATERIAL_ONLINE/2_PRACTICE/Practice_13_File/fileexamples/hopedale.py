hopedale_file = open('STUDENT_LECTUREMATERIAL_ONLINE\\2_PRACTICE\Practice_13_File\\fileexamples\\hopedale.txt','r')

hopedale_file.readline() #header

data = hopedale_file.readline().strip()
while data.startswith('#'):
    data = hopedale_file.readline().strip()

for data in hopedale_file:
    print(data)

hopedale_file.close()

print(type(hopedale_file))

# print(type(line))