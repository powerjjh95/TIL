import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T + 1):
    nums = list(map(int, input().split()))

    sum_odd_nums = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 1:
            sum_odd_nums += nums[i]

    print(f'#{t} {sum_odd_nums}')