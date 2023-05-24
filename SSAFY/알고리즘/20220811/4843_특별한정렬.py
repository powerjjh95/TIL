# # try1 : fail
# def specialsort(N, nums):
#     for k in range(N-1):
#         for i in range(k, N-1):
#             maxidx = i
#             for j in range(i + 1, len(nums)):
#                 if nums[maxidx] < nums[j]:
#                     maxidx = j
#             nums[i], nums[maxidx] = nums[maxidx], nums[i]
#             # print(list(nums))
#
#             minidx = i + 1
#             for j in range(i + 2, len(nums)):
#                 if nums[minidx] > nums[j]:
#                     minidx = j
#             nums[i], nums[minidx] = nums[minidx], nums[i]
#             # print(nums)
#     return nums[N-1]
#
# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     nums = list(map(int, input().split()))
#
# print(specialsort(N, nums))
# print(list(nums))

# # try2 : fail
# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     nums = list(map(int, input().split()))
#
#     for k in range(N-1):
#         for i in range(k, N-1):
#             maxidx = i
#             for j in range(i + 1, len(nums)):
#                 if nums[maxidx] < nums[j]:
#                     maxidx = j
#             nums[i], nums[maxidx] = nums[maxidx], nums[i]
#
#     print(list(nums)[])

# try3
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    cnt = [0] * 10

    for i in range(N):  # k번만 굴리면 된다.
        maxIdx = i  # 구간의 맨 앞을 최소값으로 가정
        for j in range(i + 1, N):  # 실제 최소값 인덱스 찾기
            if nums[maxIdx] < nums[j]:
                maxIdx = j
        nums[maxIdx], nums[i] = nums[i], nums[maxIdx]  # 최소값을 구간 맨 앞으로
    # print(nums)
    for n in range(0, 10, 2): # 0부터 N-1번째 index까지 2칸 단위로 띄워서 추출을 하겠다.
        cnt[n] = nums[int(n/2)] #
        cnt[n+1] = nums[int(-(n/2)-1)]


    print(f'#{test_case}', end = ' ')
    print(*cnt)