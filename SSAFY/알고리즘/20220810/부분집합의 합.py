# # 비트를 활용한 부분집합 구하기
# letters = ['a', 'b', 'c']
#
# for i in range(1 << len(letters)):  # 총 2³, 8개의 경우의 수 체크 # {len(letters) - 1} 조심 자리 수가 달라진다.
#     selected = [] #
#     for j in range(len(letters)): # 셀로판지 길이는 3
#         if i & (1 << j):  # 1칸씩 왼쪽으로 옮겨가며 총 3칸을 대조해본다.
#             selected.append(letters[j])
#
#     print(selected)
#
# # []                | => (i = 0) => 0 0 0 => 공집합
# # ['a']             | => (i = 1) => 0 0 1 => (j = 0)에서 걸려 'a'가 뽑힘
# # ['b']             | => (i = 2) => 0 1 0
# # ['a', 'b']        | => (i = 3) => 0 1 1
# # ['c']             | => (i = 4) => 1 0 0 => (j = 2)에서 걸려 'c'가 뽑힘
# # ['a', 'c']        | => (i = 5) => 1 0 1
# # ['b', 'c']        | => (i = 6) => 1 1 0
# # ['a', 'b', 'c']   | => (i = 7) => 1 1 1


# # try 1
# T = int(input())
# for tc in range(T): #
#     test_set = list(map(int, input().split()))
#     ans = 0 # ans를 기본값을 0이라고 하자. 0 : False
#     for i in range(1 << len(test_set)): # 본 문제에서 len(test_set)은 10이다.
#         subset_sum = 0 # 부분집합의 합을 0이라고 하고
#         if i == 0: # i가 0이면 공집합이 된다. #
#             continue
#         for j in range(len(test_set)): # len(test_set) = 10 #
#             if i & (1 << j): # 계속 돌면서
#                 subset_sum += test_set[j]
#     if  subset_sum == 0:
#         ans = 1
#         break
#
#     # print(subset_sum)
#     print(f'#{tc} {ans}')

# # try 2 : wrong
# T = int(input())
# for tc in range(1, T + 1):
#     test_set = list(map(int, input().split()))
#
#     for i in range(1<<len(test_set)):
#         subset = []
#         for j in range(len(test_set)):
#             if i & (1 << j):
#                 subset += [test_set[j]]
#
#     for k in subset:
#         ans = 0
#         if k == []:
#             continue
#             if sum(subset[k]) == 0:
#                 ans = 1
#             else:
#                 break
#
#     print(f'#{tc} {ans}')

# try 3
T = int(input())

for test_case in range(T):

    test_set = list(map(int, input().split()))
    subset = []
    ans = 0
    for i in range(1<<len(test_set)):  # 원소가 열개인 집합의 모든 부분집합을 확인 할 예정
        set_sum = 0
        if i == 0:  # i 가 0이라면 공집합임
            continue
        for j in range(len(test_set)):  # 모든 원소의 인덱스를 돌며
            '''
            2의 10제곱까지의 모든 자연수를 2의 9제곱까지의 제곱수의 합으로 표현할 수 있으며 표현방법이 유일하다.
            예를 들어 6은 2진법으로 110인데 4+2라는 뜻. (사실 당연. 2진법이니까)
            3개의 원소를 가진 집합의 부분집합은 8개인데 이 중 일곱번째 부분집합은 10진수로 6,
            2진수로 110으로 표현(0부터 7까지 있기 때문), 두번째와 세번째 원소를 원소로하는 집합이다.
            '''
            if i&(1<<j):
                set_sum = set_sum + test_set[j]
        if set_sum == 0:  # 부분집합의 합이 0일경우 종료
            ans = 1
            break
    print(f'#{test_case} {ans}')