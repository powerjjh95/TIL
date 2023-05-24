import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]
    # print(flag)

    # try1
    # W, B, R : 각 한 줄씩은 무조건 색칠되어 있어야 한다.
    # X가 적힌 칸들을 새롭게 색칠하여 오른쪽에 있는 그림
    # 러시아 국기를 만들기 위해서는 W, B, R 순을 만족해야 한다.
    # W 해당 줄에서는 'W'의 개수가 가장 많아야 하고, B, R도 동일하다.
    ans = 0
    change = 0
    for line in flag:
        W_count = 0
        for i in line:
            if i == 'W':
                W_count += 1
        print(W_count)


