'''
a~d 학생이 사용하는 평균 화장실 사용 시간 = [15, 30, 50, 10]
대기시간의 누적합의 최소를 구하여라
'''


person = [15, 30, 50, 10]
n = len(person)
person.sort()
sum = 0
left_person = n-1

for turn in range(n):
    time = person[turn]
    # 누적합 += 남은사람 + 시간
    sum += left_person * time
    left_person -= 1

print(sum)