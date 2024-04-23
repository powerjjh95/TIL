# TRY 2
from collections import deque

N = int(input())
cards = deque()
for i in range(1, N+1):
    cards.append(i)
while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())
print(cards[0])

"""
- REVIEW
    - DEQUE(Double-Ended-QUEue)
    - 양방향에서 데이터를 처리할 수 있는 자료구조
    - deque.append(x) : x를 데크의 오른쪽 끝에 삽입한다
    - deque.appendleft(x) : x를 데크의 왼쪽 끝에 삽입한다
    - deque.pop() : 데크의 오른쪽 끝 엘리먼트를 가져오는 동시에 데크에서는 삭제한다
    - deque.popleft() : 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서는 삭제한다
    - deque.extend(array) : 배열 array를 순환하면서 데크의 오른쪽에 추가한다
    - deque.extendleft(array) : 배열 array를 순환하면서 데크의 왼쪽에 추가한다
    - deque.remove(x) : x를 데크에서 찾아 삭제한다
    - deque.rotate(num) : 데크를 num만큼 회전한다 (양수면 오른쪽, 음수는 왼쪽으로)
    - List보다 속도가 빠르고 쓰레드 환경에서 안전
    - pop(0)는 O(N) 연산을 수행하지만 deque는 O(1) 연산을 수행
"""

# # TRY 1
# N = int(input())
# cards = [i for i in range(1, N+1)]
# while True:
#     if len(cards) > 1:
#         cards.pop(0)
#         temporary_card = cards.pop(0)
#         cards.append(temporary_card)
#     else:
#         break
# print(cards[0])
#


"""
- REVIEW
    - 시간 초과 발생
    - deque 개념 사용
"""