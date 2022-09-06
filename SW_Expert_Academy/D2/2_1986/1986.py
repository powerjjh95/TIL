import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())

    ans = 0
    for i in range(N):
        ans += (i + 1) * ((-1) ** i)

    print(f'#{t} {ans}')