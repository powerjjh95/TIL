# try2 # 마지막에
T = 10
for test_case in range(1, T + 1):
    input()
    letter = [list(input()) for _ in range(100)]
    zipped_letter = list(map(list, zip(*letter)))
    ans = []
    for i in range(100): # 행
        for j in range(100): # 열
            for k in range(j + 1): # 회문 길이
                if letter[i][k : 100 - j + k] == letter[i][j : 100 - j + k][::-1]: # i = 0, j = 0, k = 12라고 해보자 0~99 index중
                    max_num = max(max_num, 100 - j)
                if zipped_letter[i][k : 100 - j + k] == zipped_letter[i][k : 100 - j + k][::-1]:
                    max_num = max(max_num, 100 - j)
                if not max_num:
                    break
    print(f'#{test_case} {max_num}')

# # try 1
# for test_case in range(1, 11):
#     input()
#     N = [list(input()) for _ in range(100)]
#     zipped_N = list(map(list, zip(*N)))
#     ans = 0
#     # 가장 긴 회문을 어떻게 찾아...
#     # 감이 안오네...
#     for M in range(100, -1, -1):
#         for r in range(100):
#             for c in range(100 - M + 1):
#                 # print(c)
#                 # print(c+M) # 역순으로 가니깐
#                 if c + M < 100 and  N[r][c:c + M] == N[r][c:c + M][::-1]:
#                     ans = N[r][c:c + M]
#                     print(N[r][c:c + M],'arr')
#                     break
#
#                 if c + M < 100 and  zipped_N[r][c:c + M] == zipped_N[r][c:c + M][::-1]:
#                     ans = ''.join(zipped_N[r][c:c + M])
#                     print(zipped_N[r][c:c + M],'zip')
#                     break
#             if ans: break # r을 break 하지 않는다면 0까지 진행
#         if ans: break # M을 break 하지 않는다면 0까지 진행
#     print(ans)
#     print(f'#{test_case} {len(ans)}')

# # try 1
# for test_case in range(1, 11):
#     input()
#     N = [list(input()) for _ in range(100)]
#     zipped_N = list(map(list, zip(*N)))
#     ans = 0
#     # 가장 긴 회문을 어떻게 찾아...
#     # 감이 안오네...
#     for M in range(100, -1, -1):
#         for r in range(100):
#             for c in range(100 - M + 1):
#                 # print(c)
#                 # print(c+M) # 역순으로 가니깐
#                 if c + M < 100 and  N[r][c:c + M] == N[r][c:c + M][::-1]:
#                     ans = N[r][c:c + M]
#                     print(N[r][c:c + M],'arr')
#                     break
#
#                 if c + M < 100 and  zipped_N[r][c:c + M] == zipped_N[r][c:c + M][::-1]:
#                     ans = ''.join(zipped_N[r][c:c + M])
#                     print(zipped_N[r][c:c + M],'zip')
#                     break
#             if ans: break # r을 break 하지 않는다면 0까지 진행
#         if ans: break # M을 break 하지 않는다면 0까지 진행
#     print(ans)
#     print(f'#{test_case} {len(ans)}')