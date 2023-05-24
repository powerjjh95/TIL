# # try1
# T = int(input())
# for test_case in range(1, T + 1):
#     cal = input() # 입력을 받고
#     result = '' # 빈 string을 만든 후
#     stack = [] # 빈 list에 연산자를 쌓아 놓기 위함
#
#     for i in cal:
#         if i.isnumeric(): # 숫자는 그냥 쌓고
#             result += i # 결과에 i를 쌓는다.
#         elif i == '*' or i == '/': # '*'과 '/'는 우선적으로 연산되는 것이기 때문에
#             stack.append(i) #
#         else:
#             stack.append(i)
#     # print(i)
#     while stack:
#         result += stack.pop()
#
#     print(f'#{test_case} {result}')

# try2
T = int(input())
for test_case in range(1, T + 1):
    target = input()
    operator = {'*' : 3, '/' : 3, '+' : 2, '-': 2, '(' : 1} # 연산자들의 우선순위
    ans = '' #
    stack = []
    for i in target: # 입력받은 문자열(수식)에 대해 하나하나 확인
        if i.isnumeric(): # 숫자라면
            ans += i # 그대로 붙임
        elif i == '(': # 여는 괄호라면
            stack.append(i)
        elif i == ')': # 닫는 괄호라면
            while stack[-1] != '(':
                ans += stack.pop() # 쌓인 연사자들을 푼다.
            stack.pop() # 여는 괄호까지 빼낸다.
        else:
            while stack and operator[i] <= operator[stack[-1]]: # 연산자 우선순위를 고려하여 스택 가장 위에 있는 연산자를 확인하고
                ans += stack.pop()
            stack.append(i)
        while stack:
            ans += stack.pop()
    print(f'#{test_case} {ans}')