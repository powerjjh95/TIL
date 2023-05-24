import sys
sys.stdin = open('in1.txt')

# dr_plus = [-1, 0, 1, 0]
# dc_plus = [0, 1, 0, -1]
# dr_cross = [-1, 1, 1, -1]
# dc_cross = [1, 1, -1, -1]

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]

    # try1
    # delta 탐색을 이용하여 문제 해결
    # + 방향, x 방향 두 방향 다 탐색

    ans = 0
    # + 방향
    # 상우하좌(시계방향)
    dr_plus = [-1, 0, 1, 0]
    dc_plus = [0, 1, 0, -1]
    # 특정 기준점이 주어진 것이 아니기 때문에
    for r in range(N):
        for c in range(N):
            # 기준점
            spray = fly[r][c]
            for direction in range(4):
                for i in range(1, M): # 기준점 제외하고 다음 구역부터 search
                    # new_r, new_c = r + dr_plus[direction] * i, c + dr_plus[direction] * i
                    new_r = r + dr_plus[direction] * i # 방향 계속 바꿔가며 탐색
                    new_c = c + dc_plus[direction] * i # 열 계속 교환하며 탐색
                    if 0 <= new_r < N and 0 <= new_c < N: # index out of range를 방지하기 위해
                        spray += fly[new_r][new_c] # 상우하좌(시계방향)중 기준점 기준으로 M만큼의 fly 퇴치 수 갱신
            ans = max(ans, spray)

    # x 모양
    # 1시 5시 8시 10시 (시계방향)
    dr_cross = [-1, 1, 1, -1]
    dc_cross = [1, 1, -1, -1]
    for r in range(N):
        for c in range(N):
            spray = fly[r][c]
            for direction in range(4):
                for i in range(1, M): # 0이 포함되면 방향을 바꿀 때 마다 기준점이 중복되기 때문에
                    new_r = r + dr_cross[direction] * i
                    new_c = c + dc_cross[direction] * i
                    if 0 <= new_r < N and 0 <= new_c < N:
                        spray += fly[new_r][new_c]
            ans = max(ans, spray)

    print(f'#{t} {ans}')
