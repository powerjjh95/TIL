import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))

    # 오름차순으로 정리
    numbers = list(set(sorted(numbers)))
    ans = numbers[K-1]

    print(f'#{t} {ans}')