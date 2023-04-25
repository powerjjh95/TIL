N = int(input())
<<<<<<< HEAD
word_dict = dict()
for _ in range(N):
    word = input()
    word_dict[word] = len(word)

max_word_length = max(word_dict.values())
min_word_length = min(word_dict.values())
sorted_word_list = []

for key in word_dict:
    while len(sorted_word_list) != len(word_dict):
        if len(key) == min_word_length:
# while (len(sorted_word_list) != len(word_dict):
#     if len(word_dict.keys())



# word_dict_switch = dict()
# for key in sorted(word_dict):

    # for i in range(len(word_dict)):
=======
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
>>>>>>> 4b6a2e3fb15882999ca76bd2f421dcd0060abe34
