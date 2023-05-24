# try1 : succsess
word = list(input())
# print(len(word))
# print(type(word))
final_char = ''
ban_word = list('CAMBRIDGE')
# print(ban_word)

del_char =[]
for i in range(len(ban_word)): # i는 각각의 알파벳을 의미한다.
    for j in range(len(word)):
        if ban_word[i] == word[j]:
            del_char += ban_word[i]

for k in range(len(del_char)):
    word.remove(del_char[k])

final_char = ''.join(word) # 다음 코드가 for 문 안에 있고,
print(final_char)

# # try2 : succsess
# word = list(input())
# # print(len(word))
# # print(type(word))
#
# ban_word = list('CAMBRIDGE')
# # print(ban_word)
#
# del_char =[]
# for i in range(len(ban_word)): # i는 각각의 알파벳을 의미한다.
#     for j in range(len(word)):
#         if ban_word[i] == word[j]:
#             del_char += ban_word[i]
#             word.remove(del_char)
#             final_ch
#
# print(word)