# try 2
T = 10
for test_case in range(1, T + 1):
    N = int(input())
    letter = [list(map(str, input())) for _ in range(8)]
    zipped_letter = list(map(list, zip(*letter)))
    count = 0

    for i in range(8):
        for j in range(8 - N + 1):
            if letter[i][j : j + N] == letter[i][j : j + N][::-1]:
                count += 1

    for i in range(8):
        for j in range(8 - N + 1):
            if zipped_letter[i][j : j + N] == zipped_letter[i][j : j + N][::-1]:
                count += 1

    print(f'#{test_case} {count}')

# # try 1
# T = 10
# for test_case in range(1, T + 1):
#     N = int(input())
#     letter = [list(map(str, input())) for _ in range(8)]
#     zipped_letter = list(map(list, zip(*letter)))
#     # print(letter)
#     cnt = 0
#
#     # letter 가로의 회문 찾기
#     for i in range(8):
#         for j in range(8 - N + 1):
#             if letter[i][j : j + N] == letter[i][j : j + N][::-1]: #
#                 cnt += 1
#
#     # letter 세로 회문 찾기
#     for i in range(8):
#         for j in range(8 - N + 1):
#             if zipped_letter[i][j : j + N] == zipped_letter[i][j : j + N][::-1]:
#                 cnt += 1
#
#     print(f'#{test_case} {cnt}')
