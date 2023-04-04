# 과목의 개수
subject_length = int(input())

# 과목의 점수
subject_score_list = list(map(int, input().split()))
# print(subject_score_list)
M = max(subject_score_list)

new_score_list = []
for index in range(subject_length):
    new_score_list += [(subject_score_list[index] / M) * 100]

sum_new_score_list = sum(new_score_list)

answer = sum_new_score_list / subject_length

print(answer)