T = int(input())
for t in range(1, T + 1):
    array = input()

    # try1
    # array를 입력 받아 int, str로 구분
    # 먼저 A~Z를 숫자로 변환하는 dict
    hexa = {'A': 10, 'B' : 11, 'C': 12, 'D': 13, 'E': 14, 'F' : 15}
    empty_list = []
    for i in array:
        if i in hexa:
            empty_list += [hexa[i]]
        else:
            empty_list += [int(i)]

    hexa_bin_list = []
    for i in empty_list:
        temp = []
        for j in range(4):
            temp += [i % 2]
            i = i // 2
        hexa_bin_list += temp[::-1]

    seperate_list = []
    for i in range(0, len(hexa_bin_list), 7):
        seperate_list += [hexa_bin_list[i: i + 7]]
    # print(seperate_list)

    for i in seperate_list:
        binary_list = []
        decimal_list = []
        ans_list = []
        for j in range(len(i)):
            binary_list += [2 ** j]
        # print(binary_list)
            decimal_list += [binary_list[j] * i[::-1][j]]
            ans_list = sum(decimal_list)
        print(ans_list, end=' ')

