def BubbleSort(a, N): # 정렬한 배열과 배열의 크기
    for i in range(N-1, 0 , -1): # 정렬될 구간의 끝
        for j in range(0, i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

# a = [55, 7, 78, 12, 42]
# N = len(a)
# BubbleSort(a, N)
# print(a)