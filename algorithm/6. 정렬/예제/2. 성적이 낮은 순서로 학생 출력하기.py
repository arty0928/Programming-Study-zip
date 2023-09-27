number = int(input())
lists=[]

for i in range(number):
    input_data = input().split()
    lists.append( (input_data[0], int(input_data[1]))  )


print(lists)

# sorted는 lists에 저장x
sorted_array = sorted(lists, key= lambda score : score[1])

for i in sorted_array:
    print(i[0], end=" ")