# # 분할 ==> 조합과 관련이 있다.
# # 주어진 전체 N개의 자료에서 2개 혹은 3개를 뽑는(선택하는) 모든 경우를
# # 예제
# arr = ['A', 'B', 'C']
# N = len(arr)
#
# for i in range(N):
#     for j in range(i + 1, N):
#         if i == j:
#             continue
#             print(i, j, arr[i], arr[j])

import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    # print(numbers[0])
    # try1
    # 3분할 하는게 아니라 구분할 수 있는 point 2개만 있으면 되기 때문에 i와 j만 있으면 충분하다.
    ans = 999999999
    for i in range(1, N-1): # Q.이건 왜 1부터지? # A.시작점이 아니라 구분할 포인트이기 때문에 sector1이 적어도 1개를 가지기 위해서는 필요하다.
        for j in range(i, N): # Q. 왜 N까지일까? # A.j = N-1 까지
            sector1 = sum(numbers[0 : i])
            sector2 = sum(numbers[i : j])
            sector3 = sum(numbers[j : N])
            max_sector = max(sector1, sector2, sector3)
            min_sector = min(sector1, sector2, sector3)
            # print(t, max_sector, min_sector)
            tmp = max_sector - min_sector
            if ans > tmp:
                ans = tmp

    print(f'#{t} {ans}')



