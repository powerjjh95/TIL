# TRY 3
N = int(input())
N_cards = list(map(int, input().split()))
M = int(input())
M_cards = list(map(int, input().split()))

cards_count = {}
for N_card in N_cards:
    if N_card in cards_count:
        cards_count[N_card] += 1
    else:
        cards_count[N_card] = 1

for M_card in M_cards:
    if M_card in cards_count:
        print(cards_count[M_card], end=" ")
    else:
        print(0, end=" ")
    # print(cards_count[M_card])
# print(cards_count)
# for card_count in cards_count.values():
#     print(card_count, end =" ")


# # TRY 2
# '''
# - dictionary로 풀어보기
# - 자료구조 바꿔가면서 풀어보기
# = Edge Case
# 10
# 1 2 3 1 2 3 1 2 3 1
# 5
# 1 0 0 0 1
# // 4 0
# -> M에 같은 수가 중복되지 않는다는 워딩은 없다.
# '''
#
#
# N = int(input())
# N_cards = list(map(int, input().split()))
# M = int(input())
# M_cards = list(map(int, input().split()))
#
# cards_count = {}
# for M_card in M_cards:
#     cards_count[M_card] = 0
# for N_card in N_cards:
#     if N_card in cards_count.keys():
#         cards_count[N_card] += 1
# # print(cards_count)
# for card_count in cards_count.values():
#     print(card_count, end =" ")

# # TRY 1
# - 시간 초과
# - 완전 탐색 말고 새로운 방법 찾아야 함.
# -
# '''
# N = int(input())
# N_cards = list(map(int, input().split()))
# M = int(input())
# M_cards = list(map(int, input().split()))
# cards_count = []
# for M_card in M_cards:
#     count = 0
#     for N_card in N_cards:
#         if N_card == M_card:
#             count += 1
#             N_cards.remove(M_card)
#             print(M_card, count)
#             print(N_cards)
#     # print(count, end= " ")
# # print(cards_count, end="")
