# max 값이 크지 않고
nums = [4, 4, 2, 3, 5, 5, 1, 1, 5, 0]

count = [0] * (max(nums) + 1)
sorted_nums = [0] * len(nums) # 정렬된 리스트의 원형 틀

for num in nums: # 각 숫자(0, 1, 2, 3, 4, 5)의 개수 파악
    count[num] +=1

print(count) # [1, 2, 1, 1, 2, 3]

sorted_list = []  # 빈 틀

for idx, n in enumerate(count): # 하나씩 뽑으면서
    for _ in range(n):
    # 위에서 '_'의 의미는?
    # Interpreter에서 마지막 값을 저장할때
    # 값을 무시하고 싶을 때 (흔히 "I don't care"라고 부른다.)
    # 변수나 함수명에 특별한 의미 또는 기능을 부여하고자 할 때
    # 국제화(Internationalization, i18n)/지역화(Localization, l10n) 함수로써 사용할 때
        sorted_list.append(idx)  # 갯수만큼 순서대로 append!

print(sorted_list) # [1, 1, 2, 3, 4, 4, 5, 5, 5] # 불안정한 정렬


# [0, 1, 2, 3, 4, 5]
#  ↓  ↓  ↓  ↓  ↓  ↓
# [1, 2, 1, 1, 2, 3]