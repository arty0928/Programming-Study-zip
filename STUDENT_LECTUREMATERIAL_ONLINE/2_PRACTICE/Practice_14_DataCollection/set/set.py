observations_file = open('STUDENT_LECTUREMATERIAL_ONLINE\\2_PRACTICE\Practice_14_DataCollection\\set\\observations.txt')
birds_observed = set() #empty set , set은 중복 제거, 순서 상관x (실행할때마다 순서 다르게 나옴)

for line in observations_file:
    bird = line.strip()
    birds_observed.add(bird)

print(birds_observed)

for species in birds_observed:
    print(species)