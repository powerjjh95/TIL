# TRY 1
N = int(input())
A = list(map(int, input().split(" ")))
M = int(input())
M_numbers = list(map(int, input().split(" ")))

A_sorted = sorted(A)

# M_numbers를 원소별로 탐색
for M_number in M_numbers:
    start, end = 0, N - 1 # start와 end는 A List의 index.
    isExist = False

    # 이분탐색 시작
    while start <= end:
        middle = (start + end) // 2 # middle은 A List의 index
        if M_number == A_sorted[middle]:
            isExist = True
            print(1)
            break
        elif M_number > A_sorted[middle]:
            start = middle + 1
        else:
            end = middle - 1

    if not isExist:
        print(0)