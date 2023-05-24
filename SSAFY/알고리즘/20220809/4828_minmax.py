T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    ai = list(map(int, input().split()))
    min_num = 1000001
    max_num = 0


    for i in range(N):
        if ai[i] > max_num:
            max_num = ai[i]

        if ai[i] < min_num:
            min_num = ai[i]

    print(f'#{test_case} {max_num - min_num}')