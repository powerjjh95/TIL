import sys
sys.stdin = open('input.txt')

# try2
# try1 에서 후위 순회로 시도 -> 오답
# try2에서는 중위 순회로 시도
def inorder(index):
    if len(information[index]) == 2:
        stack.append(int(information[index][1]))
    else:
        inorder(int(information[index][2]) - 1) # information[0][2]-1 = 2-1 = 1
        inorder(int(information[index][3]) - 1)
        if information[index][1] in operator:
            num2 = stack.pop()
            num1 = stack.pop()
            if information[index][1] == '-':
                ans = int(num1) - int(num2)
                stack.append(ans)
            if information[index][1] == '+':
                ans = int(num1) + int(num2)
                stack.append(ans)
            if information[index][1] == '*':
                ans = int(num1) * int(num2)
                stack.append(ans)
            if information[index][1] == '/':
                ans = int(num1) // int(num2)
                stack.append(ans)

T = 10
for t in range(1, T + 1):
    N = int(input())
    information = [list(input().split()) for _ in range(N)]

    stack = []
    operator = ['-', '+', '*', '/']

    inorder(0)
    print(f'#{t}', stack[0])

# # try1
#
# # 후위연산
# def postorder(n):
#     if n <= N:
#         postorder(n * 2)
#         postorder(n * 2 + 1)
#         print(tree[n])
#         if tree[n] in operator:
#             num2 = visited.pop()
#             num1 = visited.pop()
#             if tree[n] == '-':
#                 ans = int(num1) - int(num2)
#                 visited.append(ans)
#             if tree[n] == '+':
#                 ans = int(num1) + int(num2)
#                 visited.append(ans)
#             if tree[n] == '*':
#                 ans = int(num1) * int(num2)
#                 visited.append(ans)
#             if tree[n] == '/':
#                 ans = int(num1) // int(num2)
#                 visited.append(ans)
#         else:
#             visited.append(tree[n])
#
# T = 10
# for t in range(1, T + 1):
#     N = int(input()) # N : 정점의 개수
#     tree = [0] * (N + 1)
#     tree_list = ''
#     visited = []
#     operator = ['-', '+', '*', '/']
#     for i in range(N):
#         information = input().split()
#         tree[int(information[0])] = information[1]
#
#     # print(tree)
#     postorder(1)
#     # print(visited)