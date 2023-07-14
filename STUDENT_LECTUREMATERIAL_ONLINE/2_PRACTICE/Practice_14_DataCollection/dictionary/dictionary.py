# key 값으로 찾음 (unordered), key는 변경x, value는 변경 가능

# for bird in bird_observations:
#     # bird = key 값, bird_to_observations[bird] => value 값
#     print(bird, bird_to_observations[bird]) 

# observations_file = open('observations.txt')

observations_file = open('STUDENT_LECTUREMATERIAL_ONLINE\\2_PRACTICE\\Practice_14_DataCollection\\set\\observations.txt')
bird_to_observations={}

# for line in observations_file:
#     bird = line.strip()

#     # if bird in bird_to_observations:
#     #     bird_to_observations[bird] = bird_to_observations[bird] + 1
#     # else:
#     #     bird_to_observations[bird] = 1
#     bird_to_observations[bird] = bird_to_observations.get(bird,0) + 1 #bird 키값을 줘서 있다면 value 반환 + 1, 없다면 0 return + 1

# observations_file.close()

for bird, observations in bird_to_observations.items():
    print(bird,observations)

# sorted_birds = sorted(bird_to_observations.keys()) #key값만 list로 가져와서 정렬


# # value가 1인 key 값들을 모아보기
# observations_to_birds_list = {}
# for bird, observations in bird_to_observations.items():
#     if observations in observations_to_birds_list:
#         observations_to_birds_list[observations].append(bird)
#     else:
#         observations_to_birds_list[observations] = [bird]

# # tuple과 set은 값을 봄
# # dictionary는 key를 봄
# # 변경 x : tuple
# # order x : set(할때마다 순서 바뀜), dictionary(key로)