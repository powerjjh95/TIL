# TRY 2
'''
- 메모리 문제 해결 필요!
- 하루(밤 -> 낮)에 올라가는 높이 : A-B
- (A-B)*(소요 일수 - 1) + A가 V 보다 높아지는 순간 종료
- (A-B)*(소요 일수 - 1) + A >= V, (A-B)*(소요 일수-1) >= (V-A),  (소요 일수-1) >= (V-A) / (A-B)
'''
import math
[A, B, V] = list(map(int, input().split(" ")))
height = V - A
day_length = A - B
day = 1 + math.ceil(height/day_length)
print(day)

# # TRY 1
# [A, B, V] = list(map(int, input().split(" ")))
#
# length = 0
# day = 1
# while length < V:
#     length += A
#     if length < V:
#         length -= B
#     else:
#         break
#     day += 1
# print(day)