# try 2
T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    pari = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            parichae = []
            sum_parichae = 0
            for k in range(M):
                for l in range(M):
                    sum_parichae += pari[i + k][j + l]
            # print(parichae)
            ans = max(sum_parichae, ans)

    print()




# # try 1
# T = int(input())
# for test_case in range(1, T + 1):
#     N, M = list(map(int, input().split()))
#     pari = [list(map(int, input().split())) for _ in range(N)]
#     parichae = [[0] * M for _ in range(M)]
#
#     ans = 0
#     for i in range(N - M + 1):
#         for j in range(N - M + 1):
#             sum_parichae = 0
#             for k in range(M):
#                 for l in range(M):
#                     sum_parichae += pari[i + k][j + l]
#
#             ans = max(sum_parichae, ans)
#
#     print(f'#{test_case} {ans}')