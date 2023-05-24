import sys
sys.stdin = open('input.txt')

def inorder(n):
    if n <= N:
        inorder(n * 2)
        print(tree[n], end='')
        inorder(n * 2 + 1)

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1) # 이거는 왜 N + 1 임?
    tree_str = ''
    for i in range(N):
        information = input().split()
        tree[int(information[0])] = information[1]

    print(f'#{test_case}', end = ' ')
    inorder(1)
    print()
