import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    # try1
    # 우, 하
    dp = [[0] * N for _ in range(N)]
    dp[0][0] = table[0][0]
    for r in range(N):
        for c in range(N):
            if r == 0:
                dp[r][c] = table[r][c] + dp[r][c-1]
            elif c == 0:
                dp[r][c] = table[r][c] + dp[r-1][c]
            else:
                dp[r][c] = table[r][c] + min(dp[r][c - 1], dp[r - 1][c])

    print(f'#{t} {dp[N-1][N-1]}')