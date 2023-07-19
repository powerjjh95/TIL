'''
* M이상 N이하의 소수 중 증가하는 순서대로 소수를 출력
* 소수를 판단하는 방법
    * 소수란?
        * 1보다 큰 자연수 중 1과 자기 자신만을 약수로 보유
        * 소수는 1개의 짝수(2)와 홀수로 구성되어 있다.
'''

# TRY 2
M, N = map(int, input().split(" "))

for number in range(M, N+1):
    if number == 1:
        continue
    for divisor in range(2, int(number/2) + 1): # 다음 줄의 divisor의 범위는 number를 반으로 나누어 나누어 지는 수가 있는지 확인
        if number % divisor == 0: # 'number가 합성수'라는 의미
            break
    else:
        print(number)
'''
* Q. 위의 Logic이면 2에서 걸려야 할 것 같은데 안걸리는 것이 이해가 되지 않는다.
'''

# # TRY 1
# M, N = map(int, input().split(" "))
#
# # 빈 prime_number List를 생성
# prime_number_list = []
# # 주어진 범위 내에서 for문을 돌며 number의 진위여부를 파악
# for number in range(M, N+1):
#     # number가 2인 경우를 제외
#     if number == 2:
#         prime_number_list += [prime_number]
#     # prime_number랑 2, 3, 5, 7, 11, 13, 17, ... 으로 나누어 소수 판단
#     elif number % 2 == 1:
#         # 어떻게 코드를 짜야할지 막막해서 찾아봄.
