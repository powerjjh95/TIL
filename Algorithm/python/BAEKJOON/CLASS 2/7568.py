# TRY 2
'''
- brute force(완전탐색)
'''
num_student = int(input())
student_list = []

for _ in range(num_student):
    weight, height = map(int, input().split())
    student_list.append((weight, height))

for i in student_list:
    rank = 1
    for j in student_list:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = " ")

# # TRY 1
# '''
# - ASCII Code를 활용하여 대문자 알파벳을 이용하여 dict 생성
# '''
# N = int(input())
# group = dict()
# for i in range(N):
#     weight, height = map(int, input().split(" "))
#     grade = 1
#     information = dict()
#     information['weight'] = weight
#     information['height'] = height
#     information['grade'] = grade
#     group[chr(65+i)] = information
# for j in range(N-1):
#     if group[chr(65+j)]['weight'] < group[chr(65+j+1)]['weight'] and group[chr(65+j)]['height'] < group[chr(65+j+1)]['height']:
#         group[chr(65+j)]['grade'] += 1
#     else:
#         group[chr(65+j)]['grade'] = group[chr(65+j+1)]['grade']
# print(group)