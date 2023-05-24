# N * N 칸 모두 밟아야 한다.

# T = int(input())
#
# for test_case in range(T):
#
#     N = int(input())
#     arr = []
#     for _ in range(N):
#         arr = arr + [(list(map(int, input().split())))]
#
#     dx = [1, 0, -1, 0]  # 배열내 가로, 세로로 움직이기 위한 설정
#     dy = [0, 1, 0, -1]
#     total_sum = 0
#
#     for i in range(N):
#         for j in range(N):
#             for k in range(4):  # 배열의 모든 값에 대해 전방향으로 탐색
#                 x = i + dx[k]
#                 y = j + dy[k]
#                 if (0 <= x < N) and (0 <= y < N):  # 중심점이 배열의 끝이라면 그 안쪽만 구함
#                     total_sum = total_sum + abs(arr[i][j]-arr[x][y])
#
#     print(f'#{test_case} {total_sum}')

# 교수님 풀이
T = int(input())

# 자료의 구조화
# delta : 변화된 값
# dr(delta row) ,dc(delta column)
dr = [-1, 1, 0, 0] # 행 # 상하우좌
dc = [0, 0, 1, -1] # 열 # 상하우좌
# list 안에 숫자는 임의로 설정하는건가? 어떤 원리로 설정되는거지? # 상하좌우
# 위 코드는

for tc in range(1, T + 1):
    N = int(input()) #  N * N
    # arr = [[0] * 3] * 4 # 다음 코드는 사용할 수 없다. 예를 들어 arr[0][0]이 변경되면 동일한 행의 요소들도 다 변경된다.
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = 0

    for r in range(N): # 전부 다 밟아보자.
        for c in range(N): #
            # 가짜 시행 횟수 안에서
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i] # 많이 틀리니 주의, 다음 줄에서 c를 r로 적는 오류류

                if nr < 0 or nr >= N or nc < 0 or nc >= N: # index out of range를 피하기 위한 코드
                    continue

                answer += abs(arr[r][c] - arr[nr][nc])

    print(f'#{tc} {answer}')
# 풀이
# N이 3이상인  N * N행렬에서 가장 겉에 껍데기를 제외한