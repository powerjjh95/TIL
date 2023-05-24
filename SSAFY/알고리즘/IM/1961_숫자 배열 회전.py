# try 2
# str으로 받아야 join을 사용하여 합칠수 있다.
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(str, input().split())) for _ in range(N)]
    zipped_matrix = list(map(list, zip(*matrix)))

    matrix90 = [i[::-1] for i in zipped_matrix]
    # print(matrix90)
    matrix180 = [i[::-1] for i in matrix[::-1]]
    # print(matrix180)
    matrix270 = zipped_matrix[::-1]
    # print(matrix270)

    print(f'#{test_case}')
    for j in range(N):
        print(''.join(matrix90[j]), ''.join(matrix180[j]), ''.join(matrix270[j]))

# # try 1
# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     matrix = [list(map(str, input().split())) for _ in range(N)]
#     zipped_matrix = list(map(list, zip(*matrix)))
#     ans = []
#
#     matrix90 = [j[::-1] for j in zipped_matrix]
#     # print(matrix90)
#     matrix180 = [k[::-1] for k in matrix[::-1]]
#     # print(matrix180)
#     matrix270 = zipped_matrix[::-1]
#     # print(matrix270)
#
#     print(f'#{test_case}')
#     for m in range(N):
#         print(''.join(matrix90[m]), ''.join(matrix180[m]), ''.join(matrix270[m]))