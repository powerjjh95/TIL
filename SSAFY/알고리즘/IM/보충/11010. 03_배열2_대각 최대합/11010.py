import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]

    # try1
    # 12시를 기준으로 시계방향으로 델타 탐색
    dr = [-1, 1, 1, -1] # dr : direction_row
    dc = [1, 1, -1, -1] # dc : direction_column

    ans = 0
    for r in range(N):
        for c in range(N):
            # 기준점 설정
            cross_array = array[r][c]
            for direction in range(len(dr)):
                for i in range(1, N):
                    nr = r + dr[direction] * i
                    nc = c + dc[direction] * i
                    if 0 <= nr < N and 0 <= nc < N:
                        cross_array += array[nr][nc]
                    else:
                        break

            # print(cross_array)
            ans = max(ans, cross_array)
    print(f'#{t} {ans}')
