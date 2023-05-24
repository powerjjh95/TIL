T = int(input())
for test_case in range(1, T+1):
    tc_case, tc_num = input().split()
    num = input().split()


    num_char = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    new_char = []

    for i in num_char:
        for j in num:
            if i == j:
                new_char += [j]


    print(f'#{test_case}')
    print(*new_char)