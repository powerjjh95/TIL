word = input()

alphabet_list = []
for alphabet in word:
    if alphabet not in alphabet_list:
        alphabet_list += [alphabet]

alphabet_dict = {}
for alphabet in alphabet_list:
    alphabet_dict[alphabet.upper()] = 0

for alphabet in word:
    alphabet_dict[alphabet.upper()] += 1
print(alphabet_dict)

alphabet_count_list = list(alphabet_dict.values())
max_alphabet_count_number = max(alphabet_count_list)
# print(max_alphabet)

max_alphabet_count = 0
for index in range(len(alphabet_count_list)):
    if alphabet_count_list[index] == max_alphabet_count_number:
       max_alphabet_count += 1
if max_alphabet_count == 1:
    answer = alphabet_dict.get('max_alphabet_count_number')
else:
    answer = "?"

print(answer)