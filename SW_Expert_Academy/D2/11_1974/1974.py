import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T + 1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]

    # try1
    # 가로
    ans = 1
    count = 0
    for i in puzzle:
        check_puzzle = []
        for j in range(9):
            if i[j] not in check_puzzle:
                check_puzzle.append(i[j])
                if len(check_puzzle) == 9:
                    count += 1
        # print(check_puzzle)

    # 세로
    zipped_puzzle = list(map(list, zip(*puzzle)))
    # print(zipped_puzzle)
    for i in zipped_puzzle:
        check_zipped_puzzle = []
        for j in range(9):
            if i[j] not in check_zipped_puzzle:
                check_zipped_puzzle.append(i[j])
                if len(check_zipped_puzzle) == 9:
                    count += 1
        # print(len(check_zipped_puzzle))

    # 정사각형
    for i in range(0, len(puzzle), 3):
        for j in range(0, len(puzzle), 3):
            square_puzzle = []
            for k in range(3):
                for l in range(3):
                    square_puzzle.append(puzzle[i + k][j + l])
            # print(square_puzzle)

            check_square_puzzle = []
            for x in square_puzzle:
                if x not in check_square_puzzle:
                    check_square_puzzle.append(x)
                    if len(check_square_puzzle) == 9:
                        count += 1
            # print(len(check_square_puzzle))

    if count != 27:
        ans = 0
    print(f'#{t} {ans}')