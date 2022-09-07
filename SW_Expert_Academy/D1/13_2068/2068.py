import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T + 1):
    nums = list(map(int, input().split()))

    max_num = -1
    for i in range(10):
        if max_num <= nums[i]:
            max_num = nums[i]

    print(f'#{t} {max_num}')