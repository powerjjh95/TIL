import sys
sys.stdin = open('input.txt')

T = int(input())
for i in range(1, T + 1):
    N = int(input())

    # try2

    snail = [[0] * N for _ in range(N)]
    number = 1
    # 우하좌상(시계방향)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    r, c = 0, 0
    direction = 0
    num = 1

    for _ in range(N ** 2):
        snail[r][c] = num
        r += dr[direction]
        c += dc[direction]
        num += 1
        if N == 1:
            break
        if c + dc[direction] == N or r + dr[direction] == N or c + dc[direction] < 0 or r + dr[direction] < 0:
            direction += 1
            direction = direction % 4
        elif snail[r + dr[direction]][c + dc[direction]]
            direction += 1
            direction




# # try1
# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     snail = [[0] * N for _ in range(N)]
#     # print(snail)
#     dr = [0, 1, 0, -1] # 우하좌상
#     dc = [1, 0, -1, 0] # 우하좌상
#     r = 0 #
#     c = 0
#     direction = 0
#     num = 1
#
#     for _ in range(N**2):
#         snail[r][c] = num # 처음에
#         r += dr[direction]
#         c += dc[direction]
#         num += 1
#         if N == 1:
#             continue # 1 * 1 일때는 이차원 리스트가 아니기때문에
#         if c + dc[direction] == N or r + dr[direction] == N or c + dc[direction] < 0 or r + dr[direction] < 0:
#             direction += 1
#             direction = direction % 4
#         elif snail[r+dr[direction]][c+dc[direction]] != 0:
#             direction += 1
#             direction = direction % 4
#     print(f'#{test_case}')
#     for i in snail:
#         print(*i)


    # print(snail)
# for r in range(N): # 예를 들어 N이 5라고 하자.
    #     for c in range(N):
    #         snail_num += 1
    #         if c == N:
    #             break
        # print(r, c)

# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     snail = [[0] * N for _ in range(N)]
#     # print(snail)
#     dr = [0, 1, 0, -1] # 우하좌상
#     dc = [1, 0, -1, 0] # 우하좌상
#     r = 0 #
#     c = 0
#     direction = 0
#     num = 1
#
#     for _ in range(N**2):
#         snail[r][c] = num # 처음에
#         r += dr[direction]
#         c += dc[direction]
#         num += 1
#         if N == 1:
#             continue # 1 * 1 일때는 이차원 리스트가 아니기때문에
#         if c + dc[direction] == N or r + dr[direction] == N or c + dc[direction] < 0 or r + dr[direction] < 0 or snail[r+dr[direction]][c+dc[direction]] != 0:
#             direction += 1
#             direction = direction % 4
#         # elif :
#         #     direction += 1
#         #     direction = direction % 4
#     print(f'#{test_case}')
#     for i in snail:
#         print(*i)
