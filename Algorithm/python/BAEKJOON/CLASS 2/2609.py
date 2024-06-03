# TRY 1
'''
이 문제에서는 2개의 수의 최대공약수 최소공배수를 구하라고 했지만, 3개 이상에서 최대공약수 최소공배수 구하고 싶다.
'''
number_list = list(map(int, input().split(" ")))
min_number = min(number_list)

def divisor(number):
    divisor_list = [1]
    for i in range(2, number//2 + 1):
        if number % i == 0:
            divisor_list.append(i)
    divisor_list.append(number)
    return divisor_list

def gcd(number_list):
    common_divisor_list = []
    divisor_list = divisor(min_number)
    for i in  divisor_list:
        count = 0
        for number in number_list:
            if number % i == 0:
                count += 1
            if count == len(number_list):
                common_divisor_list.append(i)
    return common_divisor_list[-1]

def lcm(number_list):
    least_common_multiple = gcd(number_list)
    number_list = [int(number/gcd(number_list)) for number in number_list]
    while sum(number_list) > len(number_list):
        for i in range(max(number_list), 1, -1):
            for j in range(len(number_list)):
                if number_list[j] % i == 0:
                    number_list[j] //= i
                    least_common_multiple *= i
    return least_common_multiple

print(gcd(number_list))
print(lcm(number_list))