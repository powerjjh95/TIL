N = int(input())
numbers = list(map(int, input()))
sum_numbers = 0
for index in range(N):
    sum_numbers += numbers[index]
print(sum_numbers)