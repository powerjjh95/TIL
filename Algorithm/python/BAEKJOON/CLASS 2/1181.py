N = int(input())
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
