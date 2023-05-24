# def bfs(i, j, N):
#     visited = [[0] * N for _ in range(N)]
#     q = []
#     q.append((i, j))
#     visited[i][j] = 1
#     while q:
#         i, j = q.pop(0)
#         if maze[i][j] == 3: # 3번인가?
#             return 1
#         for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#             ni, nj = i + di, j + dj
#             if 0 <= ni < N and 0 <= nj < N and maze[mi][mj] != 1 and visited[ni][nj] == 0:
#                 q.append((ni, nj))
#                 visited[ni][nj] = visited[i][j] + 1
#
# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     maze = [list(map(int, input().split()))]
#     sti = -1
#     stj = -1
#     for i in range(N):
#         for j in range(N):
#             if maze[i][j] == 2:
#                 sti, stj = i, j
#                 break
#
#     print(f'#{test_case} {bfs(sti, stj, N)}')

Answer = 0
T = int(input())
for test_case in range(1, T + 1):
    N, K_MIN, K_MAX = map(int, input().split())
    SCORE = [int(num) for num in input().split()]

# print(N, K_MIN, K_MAX)
# print(SCORE)

    SCORE_sorted = sorted(SCORE)
    for m in range(N):
        for n in range(m + 1, N):
            T1 = SCORE_sorted[m]
            T2 = SCORE_sorted[N - 1 - n]
            if T1 >= T2:
                break

            class_A = []
            class_B = []
            class_C = []
            for i in range(N):
                temp = []
                if SCORE_sorted[i] < T1:
                    class_A.append(SCORE_sorted[i])
                elif T1 <= SCORE_sorted[i] < T2:
                    class_B.append(SCORE_sorted[i])
                else:
                    class_C.append(SCORE_sorted[i])
            total_class = [len(class_A), len(class_B), len(class_C)]
            max_class = max(total_class)
            min_class = min(total_class)
            # print(total_class, max_class, min_class)
            if min_class < K_MIN or max_class > K_MAX:
                temp.append(-1)
            else:
                temp.append(max_class - min_class)
    Answer = min(temp)
# print(T1, T2, Answer)
# print(class_A)
# print(class_B)
# print(class_C)
    print(f'#{test_case} {Answer}')