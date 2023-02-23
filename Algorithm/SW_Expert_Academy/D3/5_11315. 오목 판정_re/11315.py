import sys
sys.stdin = open('sample_input.txt')

for test_case in range(1, int(input())+1):
    N = int(input())
    concave = [list(input()) for _ in range(N)]

    # try1
    # 가로, 세로, 대각선 탐색하여 확인하기

    answer = "NO"
    # delta 탐색색

    # 가로, 세로, 대각선(우하, 좌하)
    dr = [0, 1, 1, 1]
    dc = [1, 0, 1, -1]

    for r in range(N):
        for c in range(N):
            check = []
            if concave[r][c] == "o":
                for direction in range(len(dr)):
                    for i in range(N):
                        nr = r + dr[direction] * i
                        nc = c + dc[direction] * i
                        if 0 <= nr < N and 0 <= nc < N and concave[nr][nc] == "o":
                            check.append(concave[nr][nc])
            if len(check) == 5:
                answer = "YES"
    print(test_case, answer)