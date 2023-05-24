import sys
sys.stdin = open('sample_input.txt')

for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())
    target =[list(input()) for _ in range(N)]
    # print(target)

    # try1
    # 가로, 세로로 '#'과 '.'가 번갈아가면서 나와야한다.
    # 사방탐색(12시 기준 시계방향)

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    ans = "possible"


    for r in range(N):
        for c in range(M):

            # "#"인 경우
            if target[r][c] == "#":
                for direction in range(len(dr)): # 사방탐색을 이용
                    # 상(dr[0]) 하(dr[1]) 좌(dr[2]) 우(dr[3])
                    nr = r + dr[direction] # nr이 을 이용
                    nc = c + dc[direction] # nc
                    if 0 <= nr < N and 0 <= nc < M: # index를 넘어가지 않게 방지
                        if target[nr][nc] == "?":
                            target[nr][nc] = "."

            # "."인 경우
            if target[r][c] == ".":
                for direction in range(len(dr)):
                    nr = r + dr[direction]
                    nc = c + dc[direction]
                    if 0 <= nr < N and 0<= nc < M:
                        if target[nr][nc] == "?":
                            target[nr][nc] = "#"

    # "impossible"의 경우
    for r in range(N):
        for c in range(M):
            for direction in range(len(dr)):
                nr = r + dr[direction]
                nc = c + dc[direction]
                if 0 <= nr < N and 0 <= nc < M and target[nr][nc] != "?":
                    if target[r][c] == target[nr][nc]:
                        ans = "impossible"
                        break


    print(f'#{test_case} {ans}')

    # 정답
    # for tc in range(1, int(input()) + 1):
    #     N, M = map(int, input().split())
    #     arr = [list(input()) for _ in range(N)]
    #
    #     dr = [1, 0, -1, 0]
    #     dc = [0, 1, 0, -1]
    #     ans = "possible"
    #
    #     for r in range(N):
    #         for c in range(M):
    #             if arr[r][c] == ".":
    #                 for dir in range(4):
    #                     nr, nc = r + dr[dir], c + dc[dir]
    #                     if 0 <= nr < N and 0 <= nc < M:
    #                         if arr[nr][nc] == "?":
    #                             arr[nr][nc] = "#"
    #
    #             if arr[r][c] == "#":
    #                 for dir in range(4):
    #                     nr, nc = r + dr[dir], c + dc[dir]
    #                     if 0 <= nr < N and 0 <= nc < M:
    #                         if arr[nr][nc] == "?":
    #                             arr[nr][nc] = "."
    #
    #     for r in range(N):
    #         for c in range(M):
    #             for dir in range(4):
    #                 nr, nc = r + dr[dir], c + dc[dir]
    #                 if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != "?":
    #                     if arr[r][c] == arr[nr][nc]:
    #                         ans = "impossible"
    #                         break
    #
    #     print(f'#{tc} {ans}')

