K, N = map(int, input().split())
length_list = []
N_length = 0
count = 0
for _ in range(K):
    K_length = int(input())
    length_list += [K_length]
N_length_first = sum(length_list) // N // 100
N_length = N_length_first * 100
while True:
    for i in range(len(length_list)):
        length_list_i = length_list[i]
        if length_list_i > N_length:
            length_list_i = length_list_i - N_length
            count += 1
            # print(length_list_i)
        else:
            break
