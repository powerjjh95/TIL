import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    prices = list(map(int, input().split()))

    # try4
    profit = 0
    max_prices = 0
    for i in range(N-1, -1, -1):
        if prices[i] > max_prices:
            max_prices = prices[i]
        else:
            profit += max_prices - prices[i]

    print(f'#{t} {profit}')

    # # try3
    # profit = 0
    # prices_del_list = []
    # for i in range(len(prices)):
    #     # while prices:
    #         if prices[i] == max(prices):
    #             for j in range(len(prices[0: i + 1])):
    #                 profit += max(prices) - prices[j]


    # # try2
    # # 생각을 잘못하고 있었음...
    # # 역으로 순회하되 최대값 찾으면 그 앞에것 사서 다 팔아버리고, prices 가격에서 빼버린다
    # profit = 0
    #
    # # print(prices[0 : i])
    # for i in range(N - 1, -1, -1):  # N, N-1, N-2, N-3, ...
    #     while prices:
    #         if prices[i] == max(prices): # prices의
    #             buy_price = sum(prices[0: i])
    #             # print(buy_price)
    #             sell_price = prices[i] * len(prices[0: i])
    #             profit = sell_price - buy_price
    #         for j in range(0, i+1):
    #             prices.pop(j)
    # print(prices)



    # # try1
    #
    # # 이익을 구하기 위한 logic
    # # 매매가 : 물건을 사고 파는 값
    # # 일단 아무것도 하지 않으면 profit이 0
    # # 구매는 하루에 1개 가능
    # # 판매는 상관 X
    # # 1. 가격이 가장 낮은 날 search
    # # 2. 구매하는 건 상관없지만 판매할때 오름차순으로 되어있다면 손해를 볼수 밖에 없는 구조
    # # 3. 예를 들어, 물건을 10에 샀다. 11
    # # 4. 최종적으로 buy와 sell은 동일한 숫자여야 한다.
    # # 5. 마지막 날은 사지 않아도 된다. 왜냐하면 최소값이든 최댓값이든 0이다.
    #
    # buy_price = 0
    # sell_price = 0
    # profit = 0
    # # 물건을 사는 경우
    # for i in range(N - 1, 0, -1): # 역으로 진행 # 마지막 날 구매 X
    #     if prices[i - 1] < prices[i]:
    #         buy_price += prices[i - 1]
    # print(buy_price)
    #
    # # 물건을 파는 경우
    # for j in range(N-1, 0, -1):
    #     if prices[i - 1] >= prices[i]:
    #
    #
    # print(f'#{x} {min(prices)}')