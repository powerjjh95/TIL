import sys
sys.stdin = open('sample_input.txt')

for test_case in range(1, int(input())+1):
    N = int(input())
    grid = [list(input()) for _ in range(N)]

    # try2
    # 정사각형의 양 꼭지점의 끝을 구한다.
    # 정사각형의 가로 길이, 세로 길이를 구해 비교한다. # 길이가 다르면 정사각형 X
    ans = "yes"
    visited = []

    # 정사각형의 꼭지점 추출
    # "#"을 1, "."을 0 으로 변경
    for r in range(N):
        for c in range(N):
            if grid[r][c] == "#":
                grid[r][c] = 1
                visited.append([r, c])
            elif grid[r][c] == ".":
                grid[r][c] = 0
    # print(visited)

    # 꼭지점의 max, min 값을 구한다.
    max_v = max(visited)
    min_v = min(visited)
    # print(max_v, min_v)
    # print(max_v[0] - min_v[0])

    area = 0
    if max_v[0] - min_v[0] != max_v[1] - min_v[1]: # max_v[0] - min_v[0] : 세로 길이, max_v[1] - min_v[1] : 가로 길이
        ans = "no"
    else:
        area = (max_v[0] - min_v[0] + 1) * (max_v[1] - min_v[1] + 1)

    result = 0
    for i in range(min_v[0], max_v[0]+1):
        for j in range(min_v[1], max_v[1]+1):
            result += grid[i][j]

    if result != area:
        ans ="no"

    print(f'#{test_case} {ans}')

    # # try1
    # # dleta 탐색을 이용하여 #를 찾고
    # # 12시 기준 시계 방향(상우하좌)
    # dr = [-1, 0, 1, 0]
    # dc = [0, 1, 0, -1]
    # ans = "no"
    #
    # rec = []
    # for r in range(N):
    #     for c in range(N):
    #
    #         # "#"의 경우
    #         if grid[r][c] == "#":
    #             for direction in range(len(dr)):
    #                 nr = r + dr[direction]
    #                 nc = c + dc[direction]
    #             if 0 <= nr < N and 0 <= nc < N:
    #                 if grid[nr][nc] == "#":
    #                     ans ="yes"
    #
    # print(f'#{test_case} {ans}')

