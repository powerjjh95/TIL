# # 예제
# N = 10
# arr = [[0] * N for _ in range(10)]
#
# # 팔방탐색 # 12시부터 시계방향으로
# dr = [-1, -1, 0, 1, 1, 1, 0, -1]
# dc = [0, 1, 1, 1, 0, -1, -1, -1]
# r, c = 3, 4
#
# arr[r][c] = '*' # 원하는 거리(칸수)만큼 가고 싶다.
# k = 4 # 기준점을 포함해서
# for i in range(8): # 방향
#     for j in range(1, k+1): # 거리(칸 수)
#         nr = r + dr[i] * j
#         nc = c + dc[i] * j
#         # 범위 체크
#         if nr < 0 or nr >= N or nc < 0 or nc >= N:
#             break
#         arr[nr][nc] = i + 1
#
# for line in arr:
#     print(*line)

import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    table = [input() for _ in range(N)]

    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]

    ans = 'NO'
    for r in range(N):
        for c in range(N):
            if table[r][c] == '.':
                continue

            # r, c: 모든 돌의 위치
            # (r, c)를 포함해서 5칸 연속으로 돌이 있는지를 체크
            for i in range(8): # i : 방향
                for j in range(1, 5): # 4칸 전진 # 오목 완성 조건
                    nr = r + dr[i] * j
                    nc = c + dc[i] * j
                    # 범위 체크
                    if nr < 0 or nr >= N or nc <0 or nc >= N:
                        break
                    if table[nr][nc] == '.':
                        break
                else:
                    ans = 'YES' # 오목 완성

    print(f'#{t} {ans}')