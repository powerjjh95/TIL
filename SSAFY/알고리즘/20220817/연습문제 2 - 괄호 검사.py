# try 1 : clone coding
# 열림 괄호가 있으면 닫힘 괄호도 존재해야 한다.
# 예를 들어, 열림괄호가 연속 3개 온다면 닫힘 괄호도 연속 3개 와야 한다.
# 열림 괄호가 있으면, 닫힘 괄호도 따라 나와야 한다.
# 본 문제는 stack을 활용하여 푸는 문제이기 때문에, .append() 와 .pop을 이용해서 해결하는 문제이다.
# '('의 개수와 ')'의 개수가 같은면 True인가? 반례) (()))( : '(' - 3개, ')' - 3개로 동일하지만 괄호의 짝이 맞지 않다.
# T = int(input())
# for test_case in range(1, T + 1):
#     bracket = input() # bracket : 괄호
#     bracket_stack = []
#     ans = 1
#     for i in bracket:
#         if i == '(':
#             bracket_stack.append(i) # 빈 bracket_stack에 쌓는다. .append()는
#         else: # i == ')'
#             if bracket_stack == []: # if not bracket_stack: 과 동일하다. # stack이 비어있으면
#                 bracket_stack.append(i) # ')'를 빈 empty stack에 넣으면 -1을 출력
#                 break
#             else:
#                 bracket_stack.pop() # 오답의 경우를 제외한다면 마지막 항목을 pop 해라.
#     if bracket_stack == []: # bracket_stack이 빈 리스트이면
#         ans = 1 # 괄호끼리 짝이 맞는다.
#     else:
#         ans = -1 # 괄호의 짝이 맞지 않는다.
#     print(f'#{test_case} {ans}')

# try 2
T = int(input())
for test_case in range(1, T + 1):
    bracket = input()
    bracket_stack = []
    ans = 0
    for i in bracket:
        if i == '(':
            bracket_stack.append(i)
        else: # i != '('
            if not bracket_stack:
                bracket_stack.append(i)
                break # 계속 쌓이면 똑같아 지기 때문에
            else:
                bracket_stack.pop()
    if not bracket_stack:
        ans = 1
    else:
        ans = -1

    print(f'#{test_case} {ans}')