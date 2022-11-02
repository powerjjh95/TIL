# #4Permutation2

# arr = ['A', 'B', 'C', 'D']
#
# for i in range(4):
#     for j in range(4):
#             if i != j and j != i:
#                 print([arr[i], arr[j]])


# 4 Permutaion 2
arr = ['A', 'B', 'C', 'D']  # 재료 리스트
sel = [0, 0]  # 인형뽑기 selection
check = [0, 0, 0, 0]  # 뽑을지 말지 결정하는 리스트


def perm(depth):  # 각자 뎁스에서는? 꿈안의 꿈(인셉션)-- ㅡ
    if depth == 2:  # 최고 뎁스에 도달했으면?
        print(sel)  # print
        return

    for i in range(4):  # 3번의 화살표 떨어트릴 기회
        if not check[i]:  # 각 기회 안에서 check를 보고 멈출 수 있는지 보고?
            check[i] = 1  # 멈출 수 있다면 if 통과했으니까 자리 차지했다고 표시하고
            sel[depth] = arr[i]  # 화살표가 떨어진 위치의 재료리스트
            perm(depth+1)
            check[i] = 0  # 돌아나오면서 다시 다음을 위해 초기화!! (중요)
perm(0)

# # Combination
# # 3 Combination 2
# arr = ['A', 'B', 'C']
# for i in range(3):
#     for j in range(i + 1, 3):
#         print(arr[i], arr[j])

# # 5 Combination 3
# arr = ['A', 'B', 'C', 'D', 'E']
# sel = [0, 0, 0]
#
# def combination(idx, sidx):
#     if sidx == 3:  # sel 길이 범위를 벗어나면 sel이 확정됐다는 소리니까 print
#         print(sel)
#         return
#     if idx == 5:  # 얘도 벗어나지 않아야 함
#         return
#
#     sel[sidx] = arr[idx]  # sidx가 가리키는 위치에 idx가 가리키는 재료를 넣음
#     combination(idx+1, sidx+1)  # 첫번째로는 두개의 화살표가 동시에 오른쪽으로 가보고
#     combination(idx+1, sidx)  # 두번째로는 arr 쪽 화살표만 혼자 가봄.
#
# combination(0, 0)