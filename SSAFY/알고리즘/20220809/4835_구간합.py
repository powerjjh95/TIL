# N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산
T = int(input())  # 출력 결과를 맞추기 위해 테스트 케이스의 개수도 입력
for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    v = list(map(int, input().split()))
# 먼저 M이 홀수일때, 짝수일때 같은가?
# 첫 줄에 테스트 케이스 개수

    max_sum = 0
    min_sum = 10000000000
    sums = []
    for i in range(N-M+1):  # 0번째 index부터 # 예를 들어, N = 10, M = 3인 경우 range(0,8)
        num_sum = 0  # 이건 왜 있어야 할까? # 초기 값 설정을 위해
        # print(num_sum)

        for j in range(M):  # 이건 왜 range(M)일까? # M = 3으로 고정되어 있기 때문에
            num_sum += v[i + j] # i = 0일 때, j가 0, 1, 2를 순회하며 i + j = 0, 1, 2가 되고 # i = 1일 때, j가 0, 1, 2를 순회하며 i + j = 1, 2, 3이 된다.
        # sums += [num_sum] # sums는 빈 list에 인접한 숫자의 합이 잘 쌓여 있는 지 확인
        # print(sums)

        if num_sum > max_sum: # 앞에서 더한 인접한 숫자의 합이 max 보다 크기때문에
            max_sum = num_sum # 새로운 최대값이 생성

        if num_sum < min_sum: # 앞에서 더한 인접한 숫자의 합이 min 보다 작기 때문에
            min_sum = num_sum # 새로운 최솟값이 생성

    print(f'#{test_case} {max_sum-min_sum}') # f-string을 이용하여 최종결과 출력