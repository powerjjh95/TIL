T = int(input())
array = input()

# try1
code_dict = {'001101' : '0', '010011' : '1', '111011': '2', '110001': '3', '100011': '4', '110111': '5', '001011' : '6', '111101' : '7', '011001': '8', '101111': '9'}
hexa = {'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14', 'F': '15'}
empty_list = []
for i in array:
    if i in hexa:
        empty_list += [int(hexa[i])]
    else:
        empty_list += [int(i)]
# print(empty_list)

dec_hex_list = []
for i in empty_list:
    temp = []
    for _ in range(4):
        temp += [str(i % 2)]
        i = i // 2
    dec_hex_list += temp[::-1]
# print(dec_hex_list)
dec_hex_list_join = ''.join(dec_hex_list)
print(dec_hex_list_join)

ans_list = []
for i in range(len(dec_hex_list_join)):
    for key in code_dict:
        if dec_hex_list_join[i : i + 6] == key:
            ans_list += [code_dict[key]]
            dec_hex_list_join = dec_hex_list_join.replace(key, ' ', 1)
            print(dec_hex_list_join)
            break
print(ans_list)

