# try1

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    # print(farm)
    empty_farm = [[0] * N for _ in range(N)]

# farm[i][j]에서 j = N // 2를 기준으로 i = N // 2까지 같은식
# i = N // 2 이후로 다른식
    sum = 0
    for i in range(N):
        for j in range(N):
            # for k in range(N):
            # for k in range(N):
            if j == N // 2 and i <= N // 2:
                empty_farm[i][j - i : j + i + 1] = farm[i][j - i : j + i + 1]
            elif i > N // 2 and j == N // 2:
                empty_farm[i][abs(j - i) : abs(j-i+N)] = farm[i][abs(j - i) : abs(j-i+N)]
    for i in range(N):
        for j in range(N):
            sum += empty_farm[i][j]

    print(f'#{test_case} {sum}')
