def solution(s):
    answer = ''
    if len(s) % 2 == 1: # 홀수
        answer += s[len(s)//2]
    if len(s) % 2 == 0: # 짝수
        answer += s [len(s)//2-1 : len(s)//2+1]
    return answer