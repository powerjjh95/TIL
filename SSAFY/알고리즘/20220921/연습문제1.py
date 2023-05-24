def Selection(A, s):
    n = len(A)
    if s == n-1:
        return
    min = s
    for i in range(s, n):
        if A[min] > A[i]:
            min = i
    A[s], A[min] = A[min], A[s]

    Selection(A, s+1)


A = [2, 4, 6, 1, 9, 8, 7, 0]
Selection(A, 0)
print(A)

# def dfs(n, sm, cnt):
#     global ans
#     if n == N:
#         if sm == K and cnt == CNT:
#             ans += 1
#         return
#
#     dfs(n+1, sm+lst[n], cnt+1)
#     dfs(n+1, sm, cnt)
#
# T = int(input())
# for test_case in range(1, T + 1):
#     CNT, K = map(int, input().split())
#     lst = [n for n in range(1, 13)]
#     N = len(lst)
#
#     ans = 0
#     dfs(0, 0, 0)

# def dfs(n, sm):
#     global ans
#
#     if ans <= sm:
#         return
#
#     if n == N:
#         if ans > sm:
#             ans = sm
#         return
#
#
#
#     for j in range(N):
#         if not v[j]:
#             v[j] = 1
#             dfs(n + 1, sm + arr[n][j])
#             v[j] = 0
#
# T = int(input())
# for test_case in range(1, T+ 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     ans = 10* N
#     dfs(0, 0)
#
#     print(f'#{test_case} {ans}')

# def dfs(n):
#     global ans
#     if n == N:
#         ans = max(ans, int("".join(map(str, lst))))
#         return
#
#     for i in range(L):
#         for j in range(i + 1, L): # L개에서 2개 뽑는 조합
#             lst[i], lst[j] = lst[j], lst[i] # 바꾼다음 lst를 숫자로 만들어야하니, 바꾸고 cst를 만들자
#
#             # cst = int("".join(map(str, lst))) # List의 경우 501ms
#             # if (n, cst) not in v:
#             #     dfs(n + 1)
#             #     v.append((n, cst))
#             # lst[i], lst[j] = lst[j], lst[i]
#
#             cst = int("".join(map(str, lst))) # dict의 경우 208ms
#             if dct_v.get((n, cst), 1):
#                 dfs(n + 1)
#                 dct_v[(n, cst)] = 0 # 반대인 경우이니 0을 저장 (그래야 get할 때 있으면 0 ,false를 리턴)
#
# T = int(input())
# for test_case in range(1, T + 1):
#     st, t = input().split()
#     N = int(t)
#     lst = []
#     for ch in st:
#         lst.append(int(ch))
#
#     v = []
#     dct_v ={}
#     L = len(lst)
#     ans = 0
#     dfs(0)
#
#     print(f'#{test_case} {ans}')




