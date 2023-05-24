import sys
sys.stdin = open('sample_input.txt')

# try1
# N : node의 개수
# M : leaf_node
# L : 값을 출력할 노드 번호 / L 이후의 내용
T = int(input())
for t in range(1, T + 1):
    N, M, L = map(int, input().split())
    if N % 2 == 0: # Node의 개수가 짝수 일때는
        tree = [0] * (N + 2) # 마지막 Node 번호가 혼자 남기 떄문에 값이 0인 짝을 만들어 주기 위해 생성
    else: # Node가 홀수인 경우
        tree = [0] * (N + 1) # leaf node가 짝을 이룬다.
    for i in range(M):
        leaf_node, number = map(int,input().split())
        tree[leaf_node] = number
    # print(tree)

    for i in range(N, 0, -1): # N에서 1까지 탐색, 0을 제외 시키는 이유 : 0은 짝수이기 때문에 값이 생성되기 때문이다.
        if i % 2 == 0:
            tree[i // 2] = tree[i] + tree[i + 1]

    print(f'#{t} {tree[L]}')
