number1, number2 = map(int, input().split())
number1_list = list(map(str, str(number1)))
number2_list = list(map(str, str(number2)))
number1 = int("".join(number1_list[::-1]))
number2 = int("".join(number2_list[::-1]))
if number1 > number2:
    answer = number1
else:
    answer = number2
print(answer)