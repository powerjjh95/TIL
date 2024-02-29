N = int(input())
integer_list = []
for _ in range(N):
    integer = int(input())
    integer_list.append(integer)
    sorted_integer_list = sorted(integer_list)
    if len(sorted_integer_list) % 2 == 0:
        arithmetic_mean = sum(sorted_integer_list) / len(sorted_integer_list)
        median = sorted_integer_list((len(sorted_integer_list) // 2) - 1) + sorted_integer_list(len(sorted_integer_list) // 2)
        for count in sorted_integer_list:

            mode = sorted_integer_list


