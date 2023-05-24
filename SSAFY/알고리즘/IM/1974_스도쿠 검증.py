# try 2
T = int(input())
ans_list = [i for i in range(1, 10)]
# print(ans_list)
for test_case in range(1, T + 1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    zipped_puzzle = list(map(list, zip(*puzzle)))
    # print(zipped_puzzle)
    ans = 0
    count = 0

    # 가로 검증
    for i in range(9):
        row = []
        for j in range(9):
            row.append(puzzle[i][j])
        if sorted(row) == ans_list:
            count += 1
            # print(count)
        # print(row)
    # 세로 검증
    for i in range(9):
        column = []
        for j in range(9):
            column.append(zipped_puzzle[i][j])
            if sorted(column) == ans_list:
                count += 1
        # print(sorted(column))

    # 가운데 검증
    for i in range(3): # i = 0
        for j in range(3): # j = 0
            box = []
            for k in range(3): # k = 0 , 1, 2
                for l in range(3):
                    box.append(puzzle[i * 3 + k][j * 3 + l]) # 각 0~20~2, 0~23~5, 0~26~8, 3~5/0~2, 3~5, 6~8, 6~8/0~2, 3~5, 6~8행
            if sorted(box) == ans_list:
                count += 1
            else:
                break

    if count == 27:
        ans = 1
    # print(count)
    print(f'#{test_case} {ans}')




# # try1
# # 1에서 9까지 숫자가 겹치지 않아야 한다.
# # 가로 세로 대각선에 겹치는 숫자가 없으면 1, 있으면 0
#
# T = int(input())
# ans_list =[i for i in range(1, 10)]
# for test_case in range(1, T + 1):
#     puzzle = [list(map(int, input().split())) for _ in range(9)]
#     ans = 0
#     count = 0
#
#     # 가로 비교
#     for i in range(9):
#         row = []
#         for j in range(9): # -1은 if문의 [j + 1] 때문
#             row.append(puzzle[i][j])
#         if sorted(row) == ans_list:
#             count += 1
#
#     # 세로비교
#     for i in range(9):
#         column = []
#         for j in range(9):
#             column.append(puzzle[j][i])
#             if sorted(column) == ans_list:
#                 count += 1
#
#     # 3 x 3 비교
#     for i in range(3): # 각 3X3의 시작점의 행
#         for j in range(3): # 각 3X3의 시작점의 열
#             matrix = []
#             for k in range(3): # 행을 바꾸며 비교하기 위한 k
#                 for l in range(3): # 열을 바꾸며 비교하기 위한 l
#                     matrix.append(puzzle[3 * i + k][3 * j + l])
#             if sorted(matrix) == ans_list:
#                 count += 1
#             else:
#                 break
#     if count == 27:
#         ans = 1
#
#     print(f'#{test_case} {ans}')

