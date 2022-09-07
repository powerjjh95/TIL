import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))


    list_sum_muliply = []
    max_multiply = 0

    if N > M:
        for i in range(N - M + 1):
            sum_multiply = 0
            Ai_slice = Ai[i : i + M]
            Bj_slice = Bj # 슬라이싱까지 done
            for j in range(M):
                sum_multiply += Ai_slice[j] * Bj_slice[j]
            list_sum_muliply += [sum_multiply]
            max_multiply = max(list_sum_muliply)
    elif N < M:
        for i in range(M - N + 1):
            sum_multiply = 0
            Ai_slice = Ai
            Bj_slice = Bj[i : i + N]
            for j in range(N):
                sum_multiply += Ai_slice[j] * Bj_slice[j]
            list_sum_muliply += [sum_multiply]
            max_multiply = max(list_sum_muliply)
    else:
        sum_multiply = 0
        Ai_slice = Ai
        Bj_slice = Bj
        for i in range(N):
            sum_multiply += Ai_slice[i] * Bj_slice[i]
        list_sum_muliply += [sum_multiply]
        max_multiply = max(list_sum_muliply)

    print(f'#{t} {max_multiply}')


