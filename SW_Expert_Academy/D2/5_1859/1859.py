import sys
sys.stdin = open('input.txt')

T = int(input())
for x in range(1, T + 1):
    N = int(input())
    prices = list(map(int, input().split()))

    # 이익을 구하기 위한 logic
    # 매매가 : 물건을 사고 파는 값
    # 일단 아무것도 하지 않으면 profit이 0
    # 구매는 하루에 1개 가능
    # 판매는 상관 X
    # 1. 가격이 가장 낮은 날 search
    # 2. 구매하는 건 상관없지만 판매할때 오름차순으로 되어있다면 손해를 볼수 밖에 없는 구조
    # 3. 예를 들어, 물건을 10에 샀다. 11
    # 4. 최종적으로 buy와 sell은 동일한 숫자여야 한다.
    # 5. 마지막 날은 사지 않아도 된다. 왜냐하면 최소값이든 최댓값이든 0이다.
    buy_count = 0
    buy_price = 0
    sell_count = 0
    sell_price = 0
    profit = [] # profit = sell_price - buy_price
    # 물건을 사는 경우
    for i in range(N-1): # 마지막 날은 사진 않아도 된다.
        if prices[i] == min(prices):
            buy_count += 1
            buy_price += prices[i]

    # 물건을 파는 경우
    for j in range(N):
        if prices[i] == max()

    print(f'#{x} {min(prices)}')