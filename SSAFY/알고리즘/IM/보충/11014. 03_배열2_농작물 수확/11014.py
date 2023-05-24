import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input().split())) for _ in range(N)]

    # try2
    ans = 99999999999
    for i in range(1, N): # 각 sector는 가로로 1만큼 여유 필요.
        for j in range(1, N): # 각 sector는 세로로 1만큼 여유 필요.
            sector1, sector2, sector3 = 0, 0, 0
            # sector1
            for k in range(0, i): # row : 0 ~ i-1
                for l in range(0, j): # column : 0 ~ j-1
                    sector1 += farm[k][l]
            # sector2
            for k in range(i, N): # row : i ~ N-1
                for l in range(0, j): # column : 0 ~ j-1
                    sector2 += farm[k][l]
            # sector3
            for k in range(0, N): # row :
                for l in range(j, N):
                    sector3 += farm[k][l]
            # print(sector1, sector2, sector3)
            tmp = max(sector1, sector2, sector3) - min(sector1, sector2, sector3)
            if ans > tmp: # 최솟값을 계속 갱신
                ans = tmp

    print(f'#{t} {ans}')



    # # try1
    # index slicing 잘 해야 함.
    #
    # for i in range(N-1):
    #     for j in range(N-1):
    #         sector1 = [[0] * i for _ in range(j)]
    #         sector2 = [[0] * (N-i-1) for _ in range(j)]
    #         sector3 = [[0] * (N-i-1) for _ in range(N-j-1)]
    #         # for k in range(i, N):
    #         #     for j in range(j, N):
    #         #         # sector1[i][j] = farm[i][j]
    #         print(sector1)





