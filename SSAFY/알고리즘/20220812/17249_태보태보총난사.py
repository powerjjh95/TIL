# try1: fail
# for i in range(len(TB)):
#     while TB[i] == '(':
#         if TB[i] == '@':
#             right_cnt += 1
#             continue
#         if TB[i] == '@':
#             left_cnt += 1
# print(f'{right_cnt} {left_cnt}')

# try2
TB = input()

punch_list = TB.split('(')
# print(punch_list)

right_count = punch_list[0].count('@')
left_count = punch_list[1].count('@')

print(f'{right_count} {left_count}')
