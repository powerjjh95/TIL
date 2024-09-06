# TRY 2
'''
- dictionary로 풀어보기
- 자료구조 바꿔가면서 풀어보기
'''
N = int(input())
N_cards = list(map(int, input().split()))
M = int(input())
M_cards = list(map(int, input().split()))
cards_count = {}
for M_card in M_cards:
    cards_count[M_card] = 0
for N_card in N_cards:
    if N_card in cards_count.keys():
        cards_count[N_card] += 1
# print(cards_count)
for card_count in cards_count.values():
    print(card_count, end =" ")


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
