# import sys
# sys.stdin = open('sample_input.txt')

# try1
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    information = [list(map(int, input().split())) for _ in range(N)]
    # print(information)

    # 먼저 0에서 400까지 각 요소가 0인 list를 생성
    # 각 now와 future에 해당되는 인덱스에 1씩 더해준다.
    # 겹친다면 따로 이동해야 하는 것이기 때문에 리스트에 최대값이 최소 단위시간이 된다.

    corridor = [0] * 201 # 방 (1, 2)가 동일한 복도 index애 존재하기 때문에 복도를 이용하여 문제를 풀어야한다.
    ans = 0
    stack = []
    for i in information:
        start = 0
        end = 0
        # i[0]과 i[1]의 위치에 따라 결정
        # test 케이스 에서는
        if i[0] < i[1]:
            start = (i[0] + 1) // 2
            end = (i[1] + 1) // 2
        else: # i[0] >= i[1]
            start = (i[1] + 1) // 2 # 10
            end = (i[0] + 1) // 2 # 100

        for j in range(start, end+1):
            corridor[j] += 1

        max_corridor = max(corridor)
    print(f'#{t} {max_corridor}')