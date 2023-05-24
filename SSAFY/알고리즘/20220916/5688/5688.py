import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())

    ans = -1
    for i in range(1, N // 2 + 2):
        if N == (i ** 3):
            ans = i
            break
        elif N < (i**3):
            break

    print(f'#{t} {ans}')
