import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T + 1):
    num = list(map(int, input().split()))

    sum_num = 0
    average_num = 0
    for i in range(10):
        sum_num += num[i]
        average_num = round(sum_num / 10)

    print(f'#{t} {average_num}')