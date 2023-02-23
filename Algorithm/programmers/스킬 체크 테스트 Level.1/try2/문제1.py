# def solution(nums):
#     answer = -1
#
#     # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
#     print('Hello Python')
#
#     return answer


# 소수가
nums = list(map(int, input().split()))

def solution(nums):
    answer = -1
    sum_nums = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                sum_nums += [nums[i] + nums[j] + nums[k]]


    answer_list = []
    for i in sum_nums:
        print(i)
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            answer_list.append(i)
    # print(answer_list)
    answer = len(answer_list)
    print(answer)
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print('Hello Python')

    return answer

solution(nums)