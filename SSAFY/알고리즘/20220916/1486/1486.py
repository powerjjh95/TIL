import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T + 1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))

    # try1
    # 1. 부분집합을 구하고
    # 2. 부분집합의 합을 구하고
    # 3. 부분집합의 합 중 B보다 큰것을 구하고
    # 4. 부분집합의 합 중 B보다 큰것을 구하고 + 차이가 가장 적은 것을 구한다.

    difference = []
    for i in range(1 << N):
        subset = []
        for j in range(N):
            if i & (1 << j):
                subset.append(height[j])

        if B <= sum(subset):
            difference += [sum(subset) - B]

    print(f'#{t} {min(difference)}')