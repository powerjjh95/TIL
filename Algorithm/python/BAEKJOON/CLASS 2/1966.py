# TRY 1
# 6 0
# 1 1 9 1 1 1
# 다음과 같은 document_importance
# #1. 1 9 1 1 1 '1'
# #2. 9 1 1 1 '1' 1
# #3. 1 1 1 '1' 1 -> 9 출력
# #4. 1 1 '1' 1 -> 1 출력
# #5. 1 '1' 1 -> 1 출력
# #6. '1' 1 -> 1 출력
# #7. 1 -> '1' 출력


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    document_importance = list(map(int, input().split()))
    # 출력 순서
    print_order = 0
    for i in range(len(document_importance)):
