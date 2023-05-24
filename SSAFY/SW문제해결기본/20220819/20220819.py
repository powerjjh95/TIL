# # 재귀함수로 부분집합 구하기
# arr = ['A', 'B', 'C']
# check =[0, 0, 0]
#
# def powerset(idx): # 재귀 깊이가 parameter
#     if idx == len(check):
#         print('체크 배열은 다음과 같음:', *check)
#         return
#
#     check[idx] = 0
#     powerset(idx + 1)
#
#     check[idx] = 1
#     powerset(idx + 1)
#
#     # for i in range(2)
#     #   check[idx] = i
#     #   powerset(idx + 1)
#
# powerset(0)


# # 순열
# ## for문 순열
# arr = ['A', 'B', 'C']
#
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             if i != j and j!= k and k != i:
#                 print([arr[i], arr[j], arr[k]])

# ## 재귀 순열
# arr = ['A', 'B', 'C'] # 재료 리스트
# sel = [0, 0, 0] # 인형 뽑기selection
# check = [0, 0, 0] # 뽑을지 말지 결정하는 리스트
#
# def perm(depth): # 각자 뎁스에서는? 꿈안의 꿈(인셉션)
#     if depth == len(check): # 최고 뎁스에 도달했으면
#         print(sel) # print
#         return
#
#     for i in range(3): # 3번의 화살표 떨어뜨릴 기회
#         if not check[i]:
#             check[i] = 1
#             sel[depth] = arr[i]
#             perm(depth + 1)
#             check[i] = 0
#
# perm(0)

# 중복순열
arr = ['A', 'B', 'C']
sel = [0, 0, 0]

def perm_rep(depth):
    if depth == 3:
        print(*sel)
