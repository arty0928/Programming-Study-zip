

# left = lists.count('L')
# right = lists.count('R')
# up = lists.count('U')
# down = lists.count('D')
    

# x = x -up + down 
# y = y + right - left

time = int(input())

lists=(input().split())
5
x = 1
y = 1

dx =[0,0,-1,1]
dy =[-1,1,0,0]

move = ['L','R','U','D']

for list in lists:
    
    for i in range(len(move)):
        # print("i",i)
        if list == move[i]:
            # print("move",move[i])
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or nx > time or ny<1 or ny >time:
        continue
    x = nx
    y = ny
    print(x,y)

print(x,y)
        
        

# for i in lists:
#     match i:
#         case 'L':
#             if y != 1:
#                 y = y -1
#                 print(x,y)
#         case 'R':
#             if y !=time:
#                 y = y +1
#                 print(x,y)        
#         case 'U':
#             if x != 1:
#                 x = x- 1
#                 print(x,y)
#         case _:
#             if x !=time:
#                 x = x+1
#                 print(x,y)

print(x,y)