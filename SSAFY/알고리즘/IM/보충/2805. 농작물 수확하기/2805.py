import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    # print(farm)

    # try1
    harvest = [[0] * N for _ in range(N)]
    sum_harvest = 0
    for r in range(N):
        for c in range(N):
            # r <= N//2인 경우
            if c == N//2 and r <= N//2:
                harvest[r][c-r : c+r+1] = farm[r][c-r : c+r+1]
            # r > N//2인 경우
            elif c == N//2 and r > N//2:
                harvest[r][abs(c-r) : abs(c-r+N)] = farm[r][abs(c-r) : abs(c-r+N)]

    # 총합 구하기
    for r in range(N):
        for c in range(N):
            sum_harvest += harvest[r][c]

    print(f'#{t} {sum_harvest}')
