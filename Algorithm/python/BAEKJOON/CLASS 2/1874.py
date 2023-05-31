# 1부터 하나씩 push를 받으며

n = int(input())
stack = []
calculation = []
flag = 0
current = 1

for _ in range(n):
    number = int(input())
    while current <= number: # 입력한 수를 만날 때까지 오름차순으로 push
        stack.append(current)
        calculation.append("+")
        current += 1
        # 입력한 수를 만나면 while문 탈출. 즉 current = number일 때 까지 while문을 돌아 stack을 쌓는다.

    if stack[-1] == number: # stack(list)의 마지막
        stack.pop()
        calculation.append("-")
    else:
        print("NO")
        flag = 1
        break

if flag == 0:
    for i in calculation:
        print(i)