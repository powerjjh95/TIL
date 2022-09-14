import sys
sys.stdin = open('input.txt')

# dict 형태로 만든다.
alphabet = input()
alphabet_number = 1 # 제일 처음 Ark 1dl slRKs
alphabet_dict = dict() # empty dict
for each in alphabet:
    # print(each)
    alphabet_dict[each] = alphabet_number
    alphabet_number += 1

print(*alphabet_dict.values())
