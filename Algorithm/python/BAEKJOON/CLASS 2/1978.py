# TRY 1

N = int(input())
numbers = list(map(int, input().split()))

count = 0

for number in numbers:
    is_prime_number = 1
    if number > 1:
        for divisor in range(2, number):
            # print(is_prime_number)
            if number % divisor == 0:
                is_prime_number = 0
        if is_prime_number == 1:
            count += 1

print(count)
