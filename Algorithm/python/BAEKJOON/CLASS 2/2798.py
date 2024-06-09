# TRY 2
'''
- itertools의 사용법 학습
'''
from itertools import combinations
N, M = map(int, input().split(" "))
cards = list(map(int, input().split(" ")))
cards_sum_list = []
for element in combinations(cards, 3):
    if sum(element) <= M:
        cards_sum_list.append(sum(element))
print(max(cards_sum_list))



# # TRY 1
# '''
# - 원소의 개수가 3개인 부분집합을 구하기
# - 부분집합을 구해 실행하니깐 '메모리 초과'
# '''
# N, M = map(int, input().split(" "))
# cards = list(map(int, input().split(" ")))
#
# def subset(parameter_list):
#     subsets = [[]]
#     for elements in parameter_list:
#         size = len(subsets)
#         for i in range(size):
#             subsets.append(subsets[i]+[elements])
#     return subsets
#
# selected_cards = subset(cards)
# selected_card_sum = []
# for selected in selected_cards:
#     if len(selected) == 3:
#         selected_card_sum.append(sum(selected))
#     for card_sum in selected_card_sum:
#         if card_sum > M:
#             selected_card_sum.remove(card_sum)
# answer = max(selected_card_sum)
# print(answer)