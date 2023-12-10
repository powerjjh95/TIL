# TRY 1
# 6 0
# '1' 1 9 1 1 1
# 다음과 같은 document_importance
# #1. 1 9 1 1 1 '1'
# #2. 9 1 1 1 '1' 1
# #3. 1 1 1 '1' 1 -> 9 출력
# #4. 1 1 '1' 1 -> 1 출력
# #5. 1 '1' 1 -> 1 출력
# #6. '1' 1 -> 1 출력
# #7. 1 -> '1' 출력 -> 5번째 출력

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    # 문서의 '중요도' list 생성
    document_importance = list(map(int, input().split()))
    # 문서의 '증요도'의 index 표현
    document_importance_index = list(i for i in range(N))
    # 출력 순서
    document_order = M
    print_order = 0
    # 출력 차례가 아닌 경우, 뒤로 보내기위해 저장한 list
    temp_document_importance = []
    temp_document_importance_index = []
    while True:
        if document_importance[0] != max(document_importance):
            temp_document_importance.append(document_importance.pop(0))
            document_importance.append(temp_document_importance.pop())
            temp_document_importance_index.append(document_importance_index.pop(0))
            document_importance_index.append(temp_document_importance_index.pop())
        else:
            print_order += 1
            if document_importance_index[0] == M:
                break
            else:
                document_importance.pop(0)
                document_importance_index.pop(0)

    print(print_order)