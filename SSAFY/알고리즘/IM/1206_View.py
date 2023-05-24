# try 3
# 왼쪽과 오른쪽으로 창문을 열었을 때, 양쪽 모두 거리 2이상의 공간이 확보될 때
# 조망권이 확보되는 세대의 수를 반환하는 프로그램을 작성
# 비교의 중심이 되는 빌딩을 기준으로 양 옆 2개의 빌딩을 비교
# 그렇다면 양 옆 2개의 빌딩(총 4개) 중 가장 높은 빌딩이 중심 빌딩 보다 2이상 차이 날 경우 빌딩들을 다 카운트
# 입력 잘 받자.

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    building = [list(map(int, input().split())) for _ in range(1, T + 1)]

    ans = 0
    for i in range(N - 2):
        l2 = building[i - 2]
        l1 = building[i - 1]
        r1 = building[i + 1]
        r2 = building[i + 2]
        max_compare = max([l2, l1, r1, r2])
        if building[i] > max_compare:
            ans += building[i] - max_compare

    print(f'#{test_case} {ans}')


# # try2
# # 왼쪽과 오른쪽으로 창문을 열었을 때, 양쪽 모두 거리 2이상 일 때 조망권 확보
# # building을 입력받고 오름차순으로 정렬을 해버리면 망가져버림...
# # i번째 빌딩의 높이와 좌, 우 2개 건물의 높이를 비교하여
# #
# T = 10
# for test_case in range(1, T + 1):
#     N = int(input())
#     building = list(map(int, input().split()))
#
#     ans = 0
#     for i in range(2, N-2):
#         l1 = building[i - 1]
#         r1 = building[i + 1]
#         l2 = building[i - 2]
#         r2 = building[i + 2]
#         compare = [l1, r1, l2, r2]
#         # print(list_temp)
#         max_compare = max(compare)
#         differ = 0
#         if building[i] > max_compare:
#             differ = building[i] - max_compare
#             ans += differ
#
#     print(f'#{test_case} {ans}')

# try1
# T = 10
#
# for test_case in range(1, T + 1):
#     N = int(input())
#     b_lst = list(map(int, input().split()))  # 빌딩리스트
#
#     # 변수초기화
#     cnt = 0
#     # 앞 뒤 0 두개 뺀 상태에서 for 문 돌면서
#     for i in range(2, N - 2):
#         # 왼쪽 2개보다 크고 & 오른쪽 두개보다 크면
#         if b_lst[i] > b_lst[i - 1] and b_lst[i] > b_lst[i - 2] and b_lst[i] > b_lst[i + 1] and b_lst[i] > b_lst[i + 2]:
#             # 양 옆 애들 중 높이 가장 높은 애 만큼 빼주고 카운팅 해줌
#             # 값 차이가 가장 적은 애가 높이가 가장 높기 때문에 반복문 돌려서 두번째로 높은애 찾음
#             a1 = b_lst[i] - b_lst[i - 2]
#             a2 = b_lst[i] - b_lst[i - 1]
#             a3 = b_lst[i] - b_lst[i + 1]
#             a4 = b_lst[i] - b_lst[i + 2]
#             min_gap = a1
#             for a in [a1, a2, a3, a4]:
#                 if a < min_gap:
#                     min_gap = a
#             cnt += min_gap
#
#     print(f"#{test_case} {cnt}")