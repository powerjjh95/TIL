# numbers
numbers = []

for _ in range(9):
    number = int(input())
    numbers += [number]

max_number = max(numbers)

answer1 = max_number
answer2 = numbers.index(max_number) + 1

print(answer1)
print(answer2)