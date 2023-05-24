'''
9
7 4 2 0 0 6 0 7 0
'''

'''
map(function, iterable) 함수란 무엇일까요? ※ iterable 이란? 반복가능한 객체(list, dict, set, str, bytes, tuple, range)
함수와 반복 가능한 자료형을 인자로 받아서, 자료형의 각 요소에 함수를 적용한 결과를 묶어서 반환하는 기능을 합니다.
예를 들어,
a, b = map(int, [1.2, 2.5])
print(a, b) # 1, 2
함수 부분에는 기존 파이썬 내장 함수(int, float 등)뿐 아니라 사용자가 만든 함수도 인자로 넘길 수 있습니다.
이때 lambda를 사용하여 함수를 간단하게 만들 수도 있습니다.

※ lambda란 일반 함수를 가볍게 만든 것으로, 한 줄로 함수를 작성할 수 있습니다.
lambda parameter:return의 형식으로 작성합니다.
a, b = map(lambda x: x*2, [1, 2])
print(a, b)
'''

# 굳이 행과 열을 바꿀 필요 없이

#  이곳에 코드와 주석을 작성합니다.

# try1 : clone coding
# T = int(input()) # 시행 횟수
# for test_case in range(1, int(input())+1):  # 바로 여기 받을수도 있습니다!
#     room = int(input())  # 방 크기
#     heights = list(map(int, input().split()))  # 박스들 높이 정보
#     answer = 0
#
#     for i in range(room):  # 하나씩 다 돌면서
#         cnt = 0
#         # 나 다음부터 나보다 작은애를 찾아 카운트
#         for j in range(i + 1, room):
#             if heights[i] > heights[j]:
#                 cnt += 1  # 작은애를 세는것이 곧 낙차니까!
#
#     print(f'#{test_case} {answer}')

# try2
# idea
## 굳이 90도 회전을 하지 않더라도 각 행의 최고 높이보다 낮은 애들을 세면 그게 낙차가 된다.
T = int(input()) # test_case 개수
for test_case in range(1, T + 1):
    width = int(input()) # width는 가로 길이
    height = list(map(int, input().split()))

    count = 0
    ans = []
    for i in range(width):
        count = 0
        for j in range(i + 1, width):
            if height[i] > height[j]:
                count += 1
                ans += [count]
    answer = -1
    for k in range(len(ans)-1):
        if answer < ans[k]:
            answer = ans[k]
    # print(answer)
    print(f'#{test_case} {answer}')