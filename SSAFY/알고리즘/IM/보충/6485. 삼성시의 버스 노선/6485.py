import sys
sys.stdin = open('s_input.txt')

# try1
T = int(input())
for x in range(1, T + 1):
    N = int(input())

    A_B = []
    for _ in range(N):
        A, B = map(int, input().split())
        A_B.append([A, B])

    P = int(input())
    C_list = []
    for _ in range(P):
        C = int(input())
        C_list.append(C)

    # print(C_list)
    # 새로운 bus_dic를 생성하여 key와 value를 생성
    bus_dict = dict()
    for i in C_list:
        bus_dict[i] = 0

    # for j in C_list:
    for i in A_B:
        for j in range(i[0], i[1] + 1):
            if j in C_list:
                bus_dict[j] += 1

    print(f'#{x}', end=' ')
    for i in C_list:
        print(bus_dict[i])
        # print(bus_dict[i], end=' ')
    print()
