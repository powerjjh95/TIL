import sys
sys.stdin = open('sample_input.txt')

# try1
def perm(depth, acc):
    global sum_selection

    if acc >sum_selection:
        return

    if depth == N:
        if sum_selection > sum(selection):
            sum_selection = sum(selection)
            # print(selection)
            return

    for i in range(N):
        if not check[i]: # check[i]가 0이 아니라면  # A non-empty list is true. Not of true = flase:
            check[i] = 1
            selection[depth] = factory[depth][i]
            perm(depth + 1, acc + factory[depth][i])
            check[i] = 0

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    factory = [list(map(int, input().split())) for _ in range(N)]
    # print(factory) # clear
    selection = [0] * N
    check = [0] * N
    sum_selection = 99 * N + 1

    perm(0, 0)
    print(f'#{t} {sum_selection}')