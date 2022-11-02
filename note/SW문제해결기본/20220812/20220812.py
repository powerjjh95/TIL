# # Python에서 문자열 뒤집기
# greeting = 'hello world'
# # 1
# greeting[::-1]
# print(greeting)
# # 2
# greeting.reverse()
# print(greeting)
# # 3
# reversed_greeting = ''.join(list(reversed(greeting)))
# print(reversed_greeting)

def iota(int_num):
    str_num = ''

    while int_num:
        str_num = chr(int_num % 10 + 48) + str_num
        int_num //= 10

    return  str_num
print(iota(1234), type(iota(1234)))

def atoi(str_num):
    int_num = 0

    for i in str_num:
        int_num *= 10
        int_num += (ord(i) - 48)

    return str_num