import sys
sys.stdin = open('s_input.txt')

# try2
for x in range(1, int(input())+1):
    N = int(input())
    bus_route = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    Cj = [int(input()) for _ in range(P)]

    # dict를 생성하여 문제해결
    bus_dict = {}
    for c in Cj:
        bus_dict[c] = 0 # dict key값 생성

    # 버스 정류장을 지날 때 마다 값 입력
    for i in bus_route:
        for j in range(i[0], i[1]+1):
            if j in Cj:
                bus_dict[j] += 1

    print(f'#{x}', end=' ')
    for i in Cj:
        print(bus_dict[i], end=' ')
    print()

# # try1
#
# for x in range(1, int(input())+1):
#     N = int(input())
#
#     A_B = []
#     for _ in range(N):
#         Ai, Bi = map(int, input().split())
#         A_B.append([Ai, Bi])
#     # print(A_B)
#
#     P = int(input())
#     Cj = [int(input()) for _ in range(P)] # 일차원 list
#
#     bus_dict = {}
#     for c in Cj:
#         bus_dict[c] = 0
#
#     for i in A_B:
#         for j in range(i[0], i[1]+1):
#             if j in Cj:
#                 bus_dict[j] += 1
#
#     print(f'#{x}', end=' ')
#     for i in Cj:
#         print(bus_dict[i], end=' ')
#     print()
