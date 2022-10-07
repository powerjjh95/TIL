import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())

    # try1
    # 우(0), 하(1), 좌(2), 상(3)
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r, c = 0, -1
    direction = 0
    snail = [[0] * N for _ in range(N)]
    snail_number = 1
    # 다음 풀이는 for문을 쓰지 않는다.
    # while 문을 이용하여 문제 해결
    while snail_number <= N * N: # snail number가 N*N보다 작거나 같은 경우동안
        r, c = r +dr[direction], c + dc[direction] # r은
        if 0 <= r < N and 0 <= c < N and snail[r][c] == 0:
            snail[r][c] = snail_number
            snail_number += 1
        else:
