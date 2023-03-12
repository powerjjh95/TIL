A = int(input())
B = int(input())
C = int(input())

number = A * B * C
# number의 각 자리수를 잘라서 리스트에 보관
number_list = list(map(int, str(number)))
# print(number_list)

each_index = {}
for index in range(10):
    each_index[index] = 0

for each in number_list:
    for index in each_index.keys():
        if each == index:
            each_index[index] += 1
print(*list(each_index.values()), sep='\n')
