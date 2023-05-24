import sys
sys.stdin = open('sample_input.txt')

# try1
def perm(depth, acc): # acc : accumulate # acc는 backtracking을 위한 장치
    global sum_selection
    # 문제 해결에 필요한 코드

    if acc > sum_selection: # acc가 sum_selection보다 큰 경우 # backtracking
        return

    if depth == N:
        if sum_selection > sum(selection):
            sum_selection = sum(selection)
        # print(sum(selection))
        return

    for i in range(N):
            if not check[i]: # if check[i] != 0 인 경우
                check[i] = 1
                selection[depth] = array_list[depth][i]
                perm(depth + 1, acc + array_list[depth][i])
                check[i] = 0

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    array_list = [list(map(int, input().split())) for _ in range(N)]
    selection = [0] * N
    check = [0] * N
    sum_selection = 9 * N + 1
    perm(0, 0)
    print(f'#{t} {sum_selection}')