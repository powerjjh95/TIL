def perm(depth, acc): # depth : 교수님이 말한 층수 # 최소합을 저장하는
    global answer # 함수 밖에 있는 answer를 가지고 오기 위해

    if acc >= answer: # Backtracking
        return # 이미 해당 depth에서 구해진 최솟값보다 크거나 같으면 의미 X

    if depth == N: # 최후 뎁스 도달 시,
        if answer > acc:
            answer = acc # 최솟값 갱신 시도
        return #아니라도 일단 리턴

    for i in range(N):
        if not check[i]: # check[i] == 0이면
            check[i] = 1 # check
            perm(depth + 1, acc + matrix[depth][i])
            check[i] = 0

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    answer = 100
    check = [0] * N
    perm(0, 0)
    print(f'#{test_case} {answer}')
    # print(matrix)

