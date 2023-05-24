import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input()) # N : 정점(node, vertex)의 수
    tree = [0] * (N + 1)
    number = 1

    # try1
    def inorder(node): # 중위순회
        global number # number : 출력되어야 할 숫자
        if node <= N: # node가 정점의 수보다 작은 경우
            inorder(node * 2) # left_child
            tree[node] = number # parent에 숫자 할당
            number += 1 #
            inorder(node * 2 + 1) # right_child

    inorder(1) # '첫 번째 노드부터 시작하겠다.'는 의미!!
    print(f'#{t} {tree[1]} {tree[N // 2]}')


