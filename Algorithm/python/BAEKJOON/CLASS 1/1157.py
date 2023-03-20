word = input()

# 입력받은 word를 alphabet_list에 하나씩 담는다
alphabet_list = []
for alphabet in word:
    if alphabet not in alphabet_list:
        alphabet_list += [alphabet]
# print(alphabet_list)

# alphabet_list에 있는 단어들을 하나씩 뽑아, dictionary의 key를 대문자로 설정하여 value를 설정
alphabet_dict = {}
for alphabet in alphabet_list:
    alphabet_dict[alphabet.upper()] = 0

# word의 alphabet을 dictionary에 하나씩 count한다.
for alphabet in word:
    alphabet_dict[alphabet.upper()] += 1
# print(alphabet_dict)

alphabet_count_list = list(alphabet_dict.values())
max_alphabet_count_number = max(alphabet_count_list)
# print(max_alphabet)

max_alphabet_count = 0
for index in range(len(alphabet_count_list)):
    if alphabet_count_list[index] == max_alphabet_count_number:
       max_alphabet_count += 1
if max_alphabet_count == 1:
    for key, value in alphabet_dict.items():
        if value == max_alphabet_count_number:
            answer = key
else:
    answer = "?"

print(answer)