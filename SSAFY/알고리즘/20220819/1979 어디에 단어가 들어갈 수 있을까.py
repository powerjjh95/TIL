T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())

    # 기존의 puzzle 입력 받기
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    # 기존의 puzzle 전치 시키기
    zipped_puzzle = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            zipped_puzzle[i][j] += puzzle[j][i]
    print(zipped_puzzle)

    # (N + 2) * (N + 2) matrix 만들기
    new_puzzle = [[0] * (N + 2) for _ in range(N + 2)]
    for i in range(1, N+1):
        for j in range(1, N+1):
            new_puzzle[i][j] = puzzle[i-1][j-1]
    # print(new_puzzle)

    # (N + 2) * (N + 2) matrix 만들기
    new_zipped_puzzle = [[0] * (N + 2) for _ in range(N + 2)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            new_zipped_puzzle[i][j] = zipped_puzzle[i - 1][j - 1]
    # print(new_zipped_puzzle)
    # 자 이제 숫자를 세보자
    ans = 0
    def counting(a1):
        count = 0
        for i in range(N + 2):
            for j in range(N - K + 1):
                if a1[i][j] == 0 and a1[i][j + K + 1] == 0:
                    if 0 not in a1[i][j + 1 : j + K + 1]: # slicing, 예를 들어 a = [0,1,2,3,4,5], a[0 : 3] = [0, 1, 2]
                        count += 1
        return count

    ans = counting(new_puzzle) + counting(new_zipped_puzzle)
    print(f'#{test_case} {ans}')