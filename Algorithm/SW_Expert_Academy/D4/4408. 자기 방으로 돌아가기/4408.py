import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    information = [list(map(int, input().split())) for _ in range(N)]

    # try1
    corridor = [0] * 201
    for i in information:
        start = 0
        end = 0
        if i[0] < i[1]:
            start = (i[0] + 1) // 2
            end = (i[1] + 1) // 2
        else: # 원래 i[0]가 현재 방, i[1]이 돌아가야 할 방 # start와 end가 바뀌어도 상관없음? # 이 풀이에서 start와 end의 역할이 뭐야?
            start = (i[1] + 1) // 2
            end = (i[0] + 1) // 2

        for j in range(start, end + 1):
            corridor[j] += 1

    ans = max(corridor)
    print(f'#{t} {ans}')