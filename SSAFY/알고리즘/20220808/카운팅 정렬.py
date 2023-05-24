# 카운팅 정렬이란
def Counting_Sort(A, B, k):
    # A[] : 입력 배열(1 to k)
    # B[] : 정렬된 배열
    # C[] : 카운트 배열, 빈 list
    # k :
    C = [0] * (k + 1) # 모든 index의 수가 0인 list 생성 # 추후에 다시 담기 위해

    for i in range(0, len(A)): # len(A) : 입력배열의 길이 생성.
        C[A[i]] += 1 # A[i]는 인덱스순서와 k가 동일하기 때문에

    for i in range(1, len(C)): # len(C)는 0 부터 k까
