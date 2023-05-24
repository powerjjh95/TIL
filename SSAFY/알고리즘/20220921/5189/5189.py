import sys
sys.stdin = open('sample_input.txt')

# try1
# 처음과 끝은 무조건 1
# 그 사이에 있는 것들을 순열로 조합

def perm(depth):
    global answer
    # sel 리스트가 다 차면 arr에서 각각의 요소를 더해 최솟값과 비교
    if dep :
        # print(selection)
        # return
        acc = 0
        for i in range(N):
            acc += table[selection[i] - 1][selection[i + 1]-1]
        if acc < answer:
            answer = acc
        return

    for i in range(1, N):
        if not check[i]: # if not check[i] != 0 일 때
            check[i] = 1 #
            selection[depth + 1] = visit_office[i]
            perm(depth + 1)
            check[i] = 0

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    visit_office = list(range(1, N + 1))
    selection = [1] * (N + 1)
    check = [0] * N
    answer = 9999999

    perm(0)
    print(f'#{t} {answer}')

