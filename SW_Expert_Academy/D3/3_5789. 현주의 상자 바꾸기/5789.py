import sys
sys.stdin = open('sample_input.txt')

# try1
for x in range(1, int(input())+1):
    N, Q = map(int, input().split())

    box_list = [0] * N
    for i in range(1, Q+1):
        L, R = map(int,input().split())
        box_list[L-1 : R] = [i] * (R - L + 1)

    print(f'#{x}', *box_list)
