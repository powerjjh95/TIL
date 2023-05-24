import sys
sys.stdin = open('sample_input.txt')

# # try1
# T = int(input())
# for t in range(1, T+1):
#     N, M = map(int, input().split())
#     reigon = [list(map(int, input().split())) for _ in range(N)]
#     for _ in range(M):
#         r, c, bomb = map(int, input().split())
#
#         # 방향 정하기 # 12시를 기준으로 시계방향
#         dr = [-1, 0, 1, 0]
#         dc = [0, 1, 0, -1]
#         # 중복되는 지점을 어떻게 없앨것인가?
#         # 먼저, 폭탄 낙하지점을 찾아내자.
#         bomb_reigon = reigon[r][c]
#         damage_index = []
#         for direction in range(len(dr)):
#             for i in range(bomb + 1):
#                 nr = r + dr[direction] * i
#                 nc = c + dc[direction] * i
#                 if 0 <= nr < N and 0 <= nc < N:
#                     damage_index.append((nr,nc))
#         print(t, damage_index)

# try2
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    reigon = [list(map(int, input().split())) for _ in range(N)]
    information = [list(map(int, input().split())) for _ in range(M)]

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    # 중복되는 지점을 어떻게 없앨것인가?
    # 먼저, 폭탄 낙하지점을 찾아내자.
    damage_index = []
    for i in information:
        bomb_reigon = reigon[i[0]][i[1]]
        for direction in range(len(dr)):
            for j in range(i[2] + 1):
                nr = i[0] + dr[direction] * j
                nc = i[1] + dc[direction] * j
                if 0 <= nr < N and 0 <= nc < N:
                    damage_index.append((nr, nc))
    set_damage_index = set(damage_index)
    damage_index = list(set_damage_index)
    # print(damage_index)

    ans = 0
    for i in damage_index:
        ans += reigon[i[0]][i[1]]
    print(f'#{t} {ans}')