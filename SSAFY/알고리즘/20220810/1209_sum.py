
for test_case in range(1, 11):
    int(input())
    N = [list(map(int, input().split())) for _ in range(100)]

    max_num = 0
    sum_cross = 0
    sum_cross_reverse = 0

    for i in range(100):
        sum_row = 0
        sum_column = 0
        sum_cross += N[i][i]
        sum_cross_reverse += N[i][99 - i]
        for j in range(100):
            sum_row += N[i][j]
            sum_column += N[j][i]
        if max_num < sum_row:
            max_num = sum_row
        if max_num < sum_column:
            max_num = sum_column
    if max_num < sum_cross:
        max_num = sum_cross
    if max_num < sum_cross_reverse:
        max_num = sum_cross_reverse

    print(f'#{test_case} {max_num}')
