import sys
sys.stdin = open('s_input.txt')

T = int(input())
for t in range(1, T+1):
    numbers = list(map(int, input().split()))
    # print(numbers)

    # try2
    sum_numbers_list = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            for k in range(j+1, len(numbers)):
                sum_numbers_list.append(numbers[i] + numbers[j] + numbers[k])
    sorted_sum = sorted(set(sum_numbers_list))
    print(f'#{t} {sorted_sum[-5]}')

    # # try1
    # selection = [0, 0, 0]
    # sum_combination = []
    # def combination(idx, sidx):
    #     global sum_combination
    #     if sidx == len(selection):
    #         sum_combination += [sum(selection)]
    #         print(sum_combination)
    #         return
    #
    #     if idx == len(numbers):
    #         return
    #
    #     selection[sidx] = numbers[idx]
    #     combination(idx+1, sidx+1)
    #     combination(idx+1, sidx)
    #
    # combination(0, 0)