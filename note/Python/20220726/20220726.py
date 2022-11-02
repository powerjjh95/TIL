# zip 함수 
a = [1, 2, 3]
b = [4, 5, 6]
# print(zip(a, b)) # <zip object at 0x00000198044AF640>
# print(list(zip(a, b))) # [(1, 4), (2, 5), (3, 6)]

c = [1, 2, 3, 4] 
d = [1, 2]
# print(list(zip(c, d))) # [(1, 1), (2, 2)] 
# print(list(zip(a, b, c))) # [(1, 4, 1), (2, 5, 2), (3, 6, 3)]

e = {1: 0, 2:0, 3:0}
# print(e) # {1: 0, 2: 0, 3: 0}
f = dict(zip(range(1, 4), [0] * 3))
# print(f) # {1: 0, 2: 0, 3: 0}

m = [0] * 3
# print(m) # [0, 0, 0]

n = [[0] * 3] * 3
# print(n) # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

matrix1 = []
for _ in range(3):
    matrix1.append([0] * 3)
# print(matrix1) # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

matrix2 = [[0] * 3 for _ in range(3)]
# print(matrix2) # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

matrix3 = [[3, 1, 2],
           [4, 7, 9],
           [6, 8, 5]]

# print("original matrix: ",matrix3) # original matrix:  [[3, 1, 2], [4, 7, 9], [6, 8, 5]]

# for r in range(3):
#     for c in range(3):
#         if r > c:
#             matrix3[r][c], matrix3[c][r] = matrix3[c][r], matrix3[r][c]
# print(matrix3) # [[3, 1, 2], [4, 7, 9], [6, 8, 5]] # 원래대로 돌아온다.

# 전치행렬
# for r in range(3):
#     for c in range(3):
#         if r > c:
#             matrix3[r][c], matrix3[c][r] = matrix3[c][r], matrix3[r][c]
# 위 code는 정방행렬일 경우 가능
# Ex) 3 X 4 행렬을 4 X 3행렬로 바꾸는 경우
## 먼저 빈 4 X 3 행렬을 생성후 역순으로 넣는다.

# print('transposed matrix: ',matrix3) # transposed matrix:  [[3, 4, 6], [1, 7, 8], [2, 9, 5]]

# 원소가 tuple형태로 나옴 
transposed_matrix = list(zip(*matrix3))
# print('transposed_matrix: ', transposed_matrix)

list_transposed_matrix = list(map(list, zip(*matrix3)))
# print('list transposed: ', list_transposed_matrix)

nums = [1, 2, 3, 4, 5]

# LEGB : Local Enclosed Globla Built-in
# def a():
#     # nums = [9, 10, 11, 12, 13]
#     num = nums[4]
#     print(num)

# a()
# print(nums)
# print(nums[4])

set_a = {1, 2, 3, 4, 5}
print(id(set_a))

set_b = set(set_a)