# try1
T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    # 먼저 집합 A를 만들자. 집합 A는 1부터 12까지의 숫자를 원소로 가진다.
    A = [i for i in range(1, 13)]
    # print(A)
    count = 0

    # A의 부분집합 다 구해보자.
    for i in range(1 << len(A)):  # 집합 A의 개수, 2 ** 12 개의 경우의 수 체크
        sum_sub = 0
        len_sub = 0
        subset = []
        for j in range(len(A)):  # 셀로판지가 가야하는 길이는 len(A) 만큼
            if i & (1 << j):  # 1칸씩 왼쪽으로 옮겨가며 모든 경우의 수를 대조해본다.
                sum_sub += A[j]
                # print(sum_sub)
                len_sub += 1
        if len_sub == N and sum_sub == K:
            count += 1
    print(f'#{test_case} {count}')
    #             subset.append(A[j])
    #     print(subset)
        # print(type(subset))
        # print(sum(subset))
        # 이제 각 부분 집합의 합을 구한다음 구한 부분집합의 개수만 구하면 되는디...
        # if len(subset) == N and sum(sub)

        ## 먼저 빈 리스트를 만든다.

        # ## 빈 리스트에
        # for l in range(len(subset)):
        # sum_sub = []
        # sum_sub_each = 0
        # for k in range(len(subset)):
        #     sum_sub_each = sum(subset[k])
        #     sum_sub.append(sum_sub_each)
        #     print(sum_sub)

# try2
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = [i for i in range(1,13)]
    count = 0

    for i in range(1 << len(A)):
        sum_sub = 0
        len_sub = 0
        for j in range(len(A)):
            if i & (1 << j):
                sum_sub += A[j]
                len_sub += 1
        if len_sub == N and sum_sub == K:
            count += 1
    print(f'{test_case} {count}')