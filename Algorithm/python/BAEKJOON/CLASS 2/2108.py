N = int(input())
integer_list = []
integer_dict = dict()
for _ in range(N):
    integer = int(input())
    integer_list.append(integer)
    integer_dict[integer] = 0

sorted_integer_list = sorted(integer_list)

if len(sorted_integer_list) % 2 == 0:
    # 산술평균
    statistical_arithmetic_mean = round(sum(sorted_integer_list) / len(sorted_integer_list))
    # 중앙값
    statistical_median = sorted_integer_list[(len(sorted_integer_list) // 2) - 1] + sorted_integer_list[len(sorted_integer_list) // 2]
    # 최빈값
    # integer_dict의 key값의 개수 파악
    for sorted_integer in sorted_integer_list:
        integer_dict[sorted_integer] += 1
    # 최빈값의 개수에 따른 경우 구분
    integer_dict_max_value_list = []
    for key, value in integer_dict.items():
        if value == max(integer_dict.values()):
            integer_dict_max_value_list.append(key)
    if len(integer_dict_max_value_list) == 1:
        statistical_mode = integer_dict_max_value_list[0]
    else:
        statistical_mode = sorted(integer_dict_max_value_list)[1]
    # 범위
    statistical_range = max(sorted_integer_list) - min(sorted_integer_list)
else:
    # 산술평균
    statistical_arithmetic_mean = round(sum(sorted_integer_list) / len(sorted_integer_list))
    # 중앙값
    statistical_median = sorted_integer_list[len(sorted_integer_list) // 2]
    # 최빈값
    # integer_dict의 key값의 개수 파악
    for sorted_integer in sorted_integer_list:
        integer_dict[sorted_integer] += 1
    # 최빈값의 개수에 따른 경우 구분
    integer_dict_max_value_list = []
    for key, value in integer_dict.items():
        if value == max(integer_dict.values()):
            integer_dict_max_value_list.append(key)
    if len(integer_dict_max_value_list) == 1:
        statistical_mode = integer_dict_max_value_list[0]
    else:
        statistical_mode = sorted(integer_dict_max_value_list)[1]
    # 범위
    statistical_range = max(sorted_integer_list) - min(sorted_integer_list)

print(statistical_arithmetic_mean)
print(statistical_median)
print(statistical_mode)
print(statistical_range)
