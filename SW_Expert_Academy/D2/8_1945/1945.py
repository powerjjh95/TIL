import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())

    # try1
    # How to solve problem?
    # N을 소인수 분해를 하는데
    # 먼저 2로 나누었을 때, 나머지가 0이 아닐때 까지 나누어주고
    # 3, 5, 7, 11도 동일한 과정을 거친다. 13이후의 소수는 고려하지 않아도 괜찮다

    prime_number_dict = {2 : 0 , 3 : 0, 5 : 0, 7 : 0, 11: 0}
    for prime in prime_number_dict:
        # print(prime)
        while True:
            if N % prime == 0:
                prime_number_dict[prime] += 1
                N /= prime
            else:
                break

    prime_number_count = list(prime_number_dict.values())
    # print(prime_number_count) # 정답


    print(f'#{t} {prime_number_count}')
