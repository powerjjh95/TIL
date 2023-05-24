T = int(input())
for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    # print(list_str)
    list_dict = {}

    for i in str1:
        list_dict[i] = 0
        for j in str2:
            if i == j:
                list_dict[i] += 1
        max_dict = max(list_dict.values())
    # print(list_dict)
    # print(max_dict)

    print(f'#{test_case} {max_dict}')