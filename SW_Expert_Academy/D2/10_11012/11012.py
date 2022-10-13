import sys
sys.stdin = open('sample_input.txt')

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    square = [list(map(int, input().split())) for _ in range(N)]
    information = [list(map(int, input().split())) for _ in range(M)] # 행: information[i][0], 열: information[i][1], 변의 길이: information[i][2]
    # print(information)
    # for _ in range(M):
    #     r, c, length = map(int, input().split()) # r: 행, c: 열, length: 열의 길이

    # try4
    # index를 이용하여 먼저 다 구하고 if _ not in _ 구문을 이용해 중복 제거한 index 담기
    square_index = []
    for i in information:
        for j in range(i[2]):
            for k in range(i[2]):
                if [i[0]+j, i[1]+k] not in square_index:
                    square_index.append([i[0]+j, i[1]+k])
    # print(square_index)
    ans = 0
    for i in square_index:
        if 0 <= i[0] < N and 0 <= i[1] < N:
            ans += square[i[0]][i[1]]

    print(f'#{t} {ans}')

    # # try3
    # # index가 겹친다. 중복되는 index를 제거해 주어야 한다.
    # square_index = []
    # for i in range(len(information)):
    #     for j in range(information[i][2]):
    #         for k in range(information[i][2]):
    #             if [information[i][0] + j, information[i][1] + k] not in square_index:
    #                 square_index.append([information[i][0] + j, information[i][1] + k])
    #
    # ans = 0
    # for i in square_index:
    #     if 0 <= i[0] < N and 0 <= i[1] < N:
    #         ans += square[i[0]][i[1]]
    #
    # print(f'#{t} {ans}')

    # # try2
    # # 1. 정사각형이 겹치는 부분이 있는 경우, 중복 제외 필요
    # # 2. 정사각형이 범위를 넘어가는 경우 주어진 범위까지만 실행 - 완료
    #
    # empty_square = []
    # square_index = []
    # for i in range(len(information)):
    #     for j in range(3):
    #         for k in range(information[i][2]):
    #             for l in range(information[i][2]):
    #                 if [information[i][0] + k, information[i][1] + l] not in square_index:
    #                     square_index.append([information[i][0] + k, information[i][1] + l])
    # # print(square_index)
    #
    # for i in square_index:
    #     # print(i)
    #     if i[0] > N - 1 or i[1] > N - 1:
    #         continue
    #     else:
    #         empty_square.append(square[i[0]][i[1]])
    #
    # print(f'#{t} {sum(empty_square)}')


    # try1
    # for i in range(N - length + 1):
    #     for j in range(N - length + 1):
    #         empty_square = []
    #         for k in range(length):
    #             for l in range(length):
    #                 empty_square.append(square[i+k][j+l])
    #         print(empty_square)

