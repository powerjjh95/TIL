import sys
sys.stdin = open('input.txt')

# try2
for t in range(1,int(input())+1):
    N = int(input())

    # 우(0) 하(1) 좌(2) 상(3) ...
    # while을 사용하여 전개
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    snail = [[0]*N for _ in range(N)]
    snail_number = 1
    r, c = 0, -1 # Q. c가 왜 -1인가? A. 'c = c + dc[direction]' 에서 c = -1 + dc[0] = -1 + 1 = 0 으로 변경
    direction = 0 # 먼저 우(0)로 진행

    while snail_number <= N*N:
        r = r + dr[direction]
        c = c + dc[direction]
        if 0 <= r < N and 0 <= c < N and snail[r][c] == 0:
            snail[r][c] = snail_number
            snail_number += 1
        else:
            r = r - dr[direction]
            c = c - dc[direction]
            direction = (direction+1) % 4

    print(f'#{t}')
    for line in snail:
        print(*line)

# # try1
# for t in range(1, int(input())+1):
#     N = int(input())
#
#     # 우(0) 하(1) 좌(2) 상(3) 우(4) 하(5) 좌(6) 상(7) ...
#     snail = [[0] * N for _ in range(N)]
#     dr = [0, 1, 0, -1]
#     dc = [1, 0, -1, 0]
#     r, c = 0, -1
#     snail_number = 1
#     direction = 0
#     while snail_number <= N*N:
#         r = r + dr[direction]
#         c = c + dc[direction]
#         if 0 <= r < N and 0 <= c < N and snail[r][c] == 0:
#             snail[r][c] = snail_number
#             snail_number += 1
#         else:
#             r = r - dr[direction]
#             c = c - dc[direction]
#             direction = (direction+1) % 4
#
#     print(f'#{t}')
#     for line in snail:
#         print(*line)
