import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # try1
    # dict 형태로 풀자.
    numbers_dict = {}
    for i in numbers:
        numbers_dict[i] = 0
        for j in numbers:
            if i == j:
                numbers_dict[j] += 1
    mode = max(list(numbers_dict.values()))
    # print(mode)

    mode_number = [k for k, v in numbers_dict.items() if v == mode]
    print(f'#{N} {max(mode_number)}')

