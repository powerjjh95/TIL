N = int(input())
# 단어를 포함한 empty List(word_list) 생성
word_list = []
for _ in range(N):
    word = input()
    # word_list에 word를 추가
    word_list += [word]

# set을 사용하여 중복제거
word_set = set(word_list)
# 중복을 제거한 set을 다시 List로 변경
word_set_to_list = list(word_set)
# 내림차순으로 정렬
word_list = sorted(word_set_to_list)
# 내림차순으로 정렬한 것을 길이 순으로 다시 정렬
word_list = sorted(word_list, key=len)

for word in word_list:
    print(word)