S = input()
S_list = list(S)
answer_list = [-1] * 26
for i in S_list:
    temp = ord(i) - 97
    answer_list[temp] = S_list.index(i)
print(*answer_list)
