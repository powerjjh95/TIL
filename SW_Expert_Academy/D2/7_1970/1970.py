import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())

    # 어떻게 나누지?
    money_dict = {50000 : 0, 10000 : 0, 5000 : 0, 1000 : 0, 500 : 0, 100 : 0, 50 : 0, 10 : 0}

    for i in money_dict:  # 키 값을 이용해서
        money_dict[i] = N // i  # key 'i'의 value 값을 변경
        N = N - (i * money_dict[i])  # 총 금액에서 i에 해당하는 금액과 value 값을 곱해주면 된다.

    money_dict_value_list = list((money_dict.values()))
    print(f'#{t}')
    print(*money_dict_value_list)