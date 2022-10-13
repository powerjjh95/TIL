import sys
sys.stdin = open('sample_input.txt')

for test_case in range(1, int(input())+1):
    N, M =map(int, input().split())
    war = [list(map(int, input().split())) for _ in range(N)]
    bomb = [list(map(int, input().split())) for _ in range(M)]

    # delta 탐색
    # 12시기준 시계방향 (상 우 하 좌)
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    kill_index = []
    for i in bomb:
        r = i[0]
        c = i[1]
        for direction in range(len(dr)):
            for j in range(i[2]+1):
                nr = r + dr[direction] * j
                nc = c + dc[direction] * j
                if 0 <= nr < N and 0 <= nc < N:
                    if [nr, nc] not in kill_index:
                        kill_index.append([nr, nc])
    # print(kill_index)
    kill = 0
    for i in kill_index:
        kill += war[i[0]][i[1]]
    print(f'#{test_case} {kill}')


