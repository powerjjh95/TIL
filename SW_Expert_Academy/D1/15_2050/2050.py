import sys
sys.stdin = open('input.txt')

alphabet = input()

# try2
alphabet_number_list = []
for each in alphabet:
    alphabet_number = ord(each) - 64
    alphabet_number_list.append(alphabet_number)

print(*alphabet_number_list)
# # try1
# # dict 형태로 만든다.
# alphabet_number = 1 # 제일 처음 Ark 1dl slRKs
# alphabet_dict = dict() # empty dict
# for each in alphabet:
#     # print(each)
#     alphabet_dict[each] = alphabet_number
#     alphabet_number += 1
#     alphabet_dict_list = list(alphabet_dict.values())
# print(*alphabet_dict_list)
