# TRY1
# 1부터 n까지 오름차순 으로 나열되어 있는 Stack 생성(sequence)
# 입력 받은 수열(stack_list)
# sequence와 stack_list가 동일해 지는 경우까지 while문 실행

n = int(input())
stack = []
calculation = []
flag = 0
current = 1

for _ in range(n):
    number = int(input())
    while current <= number: # 입력한 수를 만날 때까지 오름차순으로 push
        stack.append(current)
print(stack)








