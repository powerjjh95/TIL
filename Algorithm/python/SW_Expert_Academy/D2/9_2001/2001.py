import sys
sys.stdin = open('input.txt')


T = int(input())
for t in range(1, T + 1):
    N, M = list(map(int, input().split()))
    pari = [list(map(int, input().split())) for _ in range(N)]

    # try2
    # M개 씩 담아야 한다.

    max_parichae = 0
    sum_parichae_list = []
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            sum_parichae = 0
            for k in range(M):
                for l in range(M):
                    sum_parichae += pari[i + k][j + l]
                    sum_parichae_list += [sum_parichae]
                    max_parichae = max(sum_parichae_list)


    print(f'#{t} {max_parichae}')


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
