import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())

    # 어떻게 나누지?
    money_dict = {50000 : 0, 10000 : 0, 5000 : 0, 1000 : 0, 500 : 0, 100 : 0, 50 : 0, 10 : 0}

    print(money_dict[50000])