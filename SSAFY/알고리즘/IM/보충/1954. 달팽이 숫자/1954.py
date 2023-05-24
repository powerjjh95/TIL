import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())

    # try3
    # 스스로 try
    # delta탐색을 위한 방향 설정 # 우 하 좌 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    direction = 0 # direction은 방향을 의미하고 direction이 0(우) 1(하) 2(좌) 3(상) 4(우) ... # N의 크기에 따라 계속 변경 되기 때문에  # direction = (direction + 1) % 4

    r, c = 0, -1 # 행(r)과 열(c)을 이용하여 조정 가능
    snail = [[0] * N for _ in range(N)]
    snail_number = 1
    while snail_number <= N * N: # snail_number가 N*N 이하인 동안
        r = r + dr[direction]
        c = c + dc[direction]
        if 0 <= r < N and 0<= c < N and snail[r][c] == 0: # r과 c가 0이상 N 미만이고 # snail[r][c]가
            snail[r][c] = snail_number
            snail_number += 1
        else:
            r = r - dr[direction]
            c = c - dc[direction]
            direction = (direction + 1) % 4

    print(f'#{t}')
    for line in snail:
        print(*line)

    # # try2
    # # IM보충 교수님 코드
    # dr = [0, 1, 0, -1]
    # dc = [1, 0, -1, 0]
    #
    # snail = [[0] * N for _ in range(N)]
    #
    # r, c = 0, -1 # 왜 이렇게 설정?
    # snail_number = 1
    # direction = 0 # 왜 이렇게 설정? # 이유 : 우(0), 하(1), 좌(2), 상(3), 우(4),
    # while snail_number <= N * N: # snail_number가 N*N보다 작거나 같은 동안에
    #     r, c = r + dr[direction], c + dc[direction]
    #     if 0 <= r < N and 0 <= c < N and snail[r][c] == 0:
    #         snail[r][c] = snail_number
    #         snail_number += 1
    #     else:
    #         r, c = r - dr[direction], c - dc[direction] # 범위를 초과한 index를 다시 조정해주고
    #         direction = (direction + 1) % 4 # direction 변경 우 -> 하 -> 좌 -> 상
    #
    # print(f'#{t}')
    # for line in snail:
    #     print(*line)

    # # try1
    # # 시계방향(우하좌상)
    # # 우(0)하(1),좌(2),상(3),우(0)...
    # # 방향 전환 dir = (dir + 1) % 4
    # dr = [0, 1, 0, -1]
    # dc = [1, 0, -1, 0]
    #
    # snail = [[0] * N for _ in range(N)]
    # snail_number = 1
    # # 우 방향
    # # 오른쪽으로 진행하기 위하다가 아래로 방향을 바꾸기 위해서는
    # # 인덱스를 벗어나야 진행이 가능하다.
    # for r in range(N+1):
    #     for c in range(N+1):
    #         for direction in range(len(dr)):
    #             snail[r][c] = snail_number
    #             snail_number += 1
    #             if r > N and c > N:
    #                 break
    #             nr = r + dr[direction]
    #             nc = c + dc[direction]