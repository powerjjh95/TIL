import sys
sys.stdin = open('sample_input.txt')

for test_case in range(1, int(input())+1):
    N = int(input())
    farm = [list(map(int, input().split())) for _ in range(5)]

    answer = 9999999999
    for i in range(1, N):
        for j in range(1, N):

            # sector1
            sector1 = 0
            for k in range(0, i):
                for l in range(0, j):
                    sector1 += farm[k][j]

            # sector2
            sector2 = 0
            for k in range(i, N):
                for l in range(0, j):
                    sector2 += farm[k][j]

            # sector3
            sector3 = 0
            for k in range(0, N):
                for l in range(j, N):
                    sector3 += farm[k][l]

            max_sector = max(sector1, sector2, sector3)
            min_sector = min(sector1, sector2, sector3)
            temporary = max_sector - min_sector

            if answer > temporary:
                answer = temporary

    print(f'#{test_case} {answer}')



