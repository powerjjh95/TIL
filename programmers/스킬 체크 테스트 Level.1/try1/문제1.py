s=input()
def solution(s):
    answer = ''
    list_answer = []
    for i in range(len(s)):  # ""를 제외
        if s[i] == ' ':
            if i % 2 == 0:  # 홀수
                list_answer += s[i].upper()
            elif i % 2 == 1:  # 짝수
                list_answer += s[i].lower()
            print(list_answer)
    return answer

solution(s)
# s = input()
# answer = ''
# for i in range(len(s)): # ""를 제외
#     if i % 2 == 0: # 홀수
#         answer += s[i].upper()
#     elif i % 2 == 1: # 짝수
#         answer += s[i].lower()
# print(answer)