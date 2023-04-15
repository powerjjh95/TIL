# board에서 W가 나온다음 "B"가 나와야 한다.
M, N = map(int, input().split(" "))

board = [input() for _ in range(M)]
count = []

# 처음 주어지는 크기와 상관없이 8 X 8 로 잘라야한다.
# M과 N에 -7을함으로써 추후에 올 for 문에서 조절이 가능
for x in range(M-7):
    for y in range(N-7):
        black_start_count = 0 # black 시작
        white_start_count = 0 # white 시작
        for i in range(x, x+8):
            for j in range(y, y+8):
                # i+j가 홀수이면, 해당 (i,j) 상하좌우는 짝수
                # (i, j) = (0, 0)이 체스판의 가장 왼쪽 상단(시작점)
                if (i+j) % 2 == 0: # i+j가 짝수인 경우(시작점 포함)
                    if board[i][j] != "B": # black 시작
                        black_start_count += 1
                    else: # white 시작
                        white_start_count += 1
                else: # i+j가 홀수인 경우
                    if board[i][j] != "W": # black 시작
                        black_start_count += 1
                    else: # white 시작
                        white_start_count += 1

        count += [black_start_count]
        count += [white_start_count]
print(min(count))
