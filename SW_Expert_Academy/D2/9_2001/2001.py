import sys
sys.stdin = open('input.txt')


T = int(input())
for t in range(1, T + 1):
    N, M = list(map(int, input().split()))
    pari = [list(map(int, input().split())) for _ in range(N)]
    parichae = [[0] * M for _ in range(M)]

    # try2
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            for k in range(M):
                for l in range(M):
                    parichae[i + k][j + l] = pari[i + k][j + l]
        print(f'{t} {parichae}')

            # ans = max(sum_parichae, ans)

    # print(f'#{t} {ans}')

    # # try1
    # ans = 0
    # for i in range(N - M + 1):
    #     for j in range(N - M + 1):
    #         sum_parichae_list = []
    #         for k in range(M):
    #             for l in range(M):
    #                 sum_parichae_list += [pari[i + k][j + l]]
    #
    #     print(sum_parichae_list)
