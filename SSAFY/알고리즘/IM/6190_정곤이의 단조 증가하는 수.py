# try1
# 각 숫자의 자릿수가 단순하게 증가하는 수
# 111566, 233359 가능
# 12343, 999888 불가능
# 예를 들어
# test_case에서 A1 = 2, A2 = 4, A3 = 7, A4 = 10일 때,
# A1 X A2 = 8, A1 X A3 = 14, A1 X A4 = 20, A2 X A3 = 28, A2 X A4 = 40, A3 X A4 = 70
# 위의 경우를 구하는건 조합쓰면 되겠다...!!
# 조합으로 구한 다음 구한 걸 다 곱하고
# 그중에 단조증가가 있고(조건1), 단조증가가 있다면 가장 큰 값(조건2) 출력
# 단조증가가 없다면 -1 출력(조건3)

# try 3
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    mono = list(map(int, input().split()))

    mono_num = []
    for i in range(N):
        for j in range(i + 1, N):
            check = mono[i] * mono[j]
            temp_check = check # 얕은 복사를 이용

            mono_remainder = []
            while temp_check: # temp_check 1보다 같거나 큰 동안에
                mono_remainder.append(temp_check % 10)
                temp_check //= 10
            # print(mono_remainder)

            flag = True # flag = 1
            for k in range(len(mono_remainder) - 1):
                if mono_remainder[i] < mono_remainder[i + 1]:
                    flag = False
                    break
            if flag: # 만약 flag가 True라면 빈 list mono_num에 입력해라.
                mono_num.append(check)
    ans = -1
    if mono_num:
        ans = max(mono_num)

    print(f'#{test_case} {ans}')


# # try2
# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     mono = list(map(int, input().split()))
#     # sel = [0] * 2 # combination 함수 사용시
#
#     mono_num = []
#     for i in range(N):
#         for j in range(i + 1, N):
#             check = mono[i] * mono[j]
#             check_temp = check
#             mono_rem = []
#             while check_temp: # while문 에서 'while <int>:'는 int >= 1 이라는 의미 # 'while <list>:' list == []가 될때 까지 돌아라.
#                 mono_rem.append(check_temp % 10)
#                 check_temp //= 10
#
#             flag = True # flag = 1
#             for k in range(len(mono_rem) - 1):
#                 if mono_rem[k] < mono_rem[k + 1]:
#                     flag = False # flag =0
#                     break
#             if flag:
#                 mono_num.append(check)
#     ans = -1
#     if mono_num:
#         ans = max(mono_num)
#
#     print(f'#{test_case} {ans}')

# try1
# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     mono = list(map(int, input().split()))
#     # sel = [0] * 2 # combination 함수 사용시
#     ans =0
#     mono_num = []
#     new_mono_num = []
#     real_mono = []
#     for i in range(N):
#         for j in range(i + 1, N):
#             mono_num.append(mono[i]*mono[j])
#
#     # print(mono_num)
#             for k in range(len(mono_num)):
#                 mono_rem = []
#                 while mono_num[k]:
#                     if mono_num[k] >= 10:
#                         mono_rem.append(mono_num[k] % 10)
#                         mono_num[k] = mono_num[k] // 10
#                     else:
#                         mono_rem.append(mono_num[k])
#                         break
#             mono_rem2 = ''.join(map(str, mono_rem[::-1]))
#             # print(len(mono_rem2))
#
#
#             for l in range(len(mono_rem2) - 1):
#                 if int(mono_rem2[l]) < int(mono_rem2[l + 1]):
#                     real_mono.append(int(mono_rem2))
#                 else:
#                     ans = -1
#
#     ans = max(real_mono)
#
#     print(f'#{test_case} {ans}')
