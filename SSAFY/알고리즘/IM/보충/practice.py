# # 이차원 리스트의 전치, 회전
# ## 크기가 N인 정방행렬 생성
# N = int(input())
# matrix = [[0]*N for _ in range(N)]
# num = 1
#
# for r in range(N):
#     for c in range(N):
#         matrix[r][c] = num
#         num += 1
#
# # print(matrix)
#
# ## 전치
# ### 방법1
# zipped_matrix_1 = [[0] * N for _ in range(N)]
# for r in range(N):
#     for c in range(N):
#         zipped_matrix_1[r][c] = matrix[c][r]
#
# # print('zipped_matrix_1', zipped_matrix_1)
#
# ### 방법2
# zipped_matrix_2 = list(zip(*matrix))
#
# # print('zipped_matrix_2', zipped_matrix_2)
# # print(zipped_matrix_2[0][0]) # 튜플 형태로 나오지만 인덱스 슬라이싱은 조절은 가능하다.
#
# ## 회전
# ### 방법1_1(시계방향 90도)
# rotated_matrix_1_1 = [[0] * N for _ in range(N)]
#
# for r in range(N):
#     for c in range(N):
#         rotated_matrix_1_1[r][c] = matrix[N - c- 1][r]
#
# # print(rotated_matrix_1_1)
#
# ### 방법1_2(시계방향 90도)
# rotated_matrix_1_2 = list(zip(*matrix[::-1]))
#
# # print(rotated_matrix_1_2)
#
# ### 방법2_1(반시계방향 90도)
# rotated_matrix_2_1 = [[0] * N for _ in range(N)]
# for r in range(N):
#     for c in range(N):
#         rotated_matrix_2_1[r][c] = matrix[c][N - r - 1]
#
# # print(rotated_matrix_2_1)
#
# ## 방법2_2(반시계방향 90도)
# rotated_matrix_2_2 = list(zip(*matrix))[::-1]
#
# # print(rotated_matrix_2_2)

