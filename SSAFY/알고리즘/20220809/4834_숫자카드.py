# 숫자가 주어진다.
# 주어진 숫자를 str 화 시킨다.
#

T = int(input())
for test_case in range(1, T + 1):
    N = int(input()) # 숫자를 받는다.
    ai = input() # 길게 나열된 숫자를 입력 받는다.
    # print(type(ai)) # <class 'str'>
    # print(ai[0])
    # print(type(ai[0]))

    list_ai = [] # 빈 리스트를 만들어 길게 나열된 숫자를 각각 저장
    for i in range(N): #
        list_ai += [int(ai[i])]
        # print(list_ai)

    count_num = [0] * 10 # 왜 이렇게 되는가...? # 단지 숫자를 세기 위한 용도이다.
    # print(count_num)
    num = 0

    for j in range(N):
        count_num[list_ai[j]] += 1

        for k in range(10): # counting 정렬의 카운트 배열
            if count_num[k] >= count_num[num]:
                num = k

    print(f'#{test_case} {num} {count_num[num]}')