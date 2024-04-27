# TRY 1
"""
- N의 자릿수를 파악한 후, constructor의 후보 개수를 최소화.
- 매 시행마다 첫째 자리를 알 수 있는 first_digit이라는 변수 생성
- constructor를 줄여 그 다음 첫쨰자리를 알 수있도록 재정의
"""
N= int(input())
length_N = len(str(N))
constructor_list = []
answer = 0
for constructor in range(N - 9*length_N, N+1):
    digit_list = [constructor]
    length_constructor = len(str(constructor))
    while constructor > 0:
        for i in range(length_constructor, 0, -1):
            first_digit = constructor // 10 ** (i - 1)
            constructor = constructor - first_digit * (10 ** (i - 1))
            digit_list += [first_digit]
    if sum(digit_list) == N:
        constructor_list += [digit_list[0]]
        if len(constructor_list) == 0:
            answer = 0
        else:
            answer = min(constructor_list)
print(answer)
