# TRY 4
import sys

N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

for i in range(N-1, 0, -1):
    for j in range(i):
        if numbers[j] > numbers[j+1]:
            numbers[j] ,numbers[j+1] = numbers[j+1], numbers[j]

for number in numbers:
    print(number)

# # TRY 3
# import sys
#
# N = int(input())
# numbers = []
# for _ in range(N):
#     numbers.append(int(sys.stdin.readline()))
#
# for number in sorted(numbers):
#     print(number)

# # TRY 2
# N = int(input())
# numbers = []
# for _ in range(N):
#     numbers.append(int(input()))
#
# for i in range(N-1, 0, -1):
#     for j in range(i):
#         if numbers[j] > numbers[j+1]:
#             numbers[j] ,numbers[j+1] = numbers[j+1], numbers[j]
#
# for number in numbers:
#     print(number)

# # TRY 1
# N = int(input())
# numbers = []
# for _ in range(N):
#     numbers.append(int(input()))
#
# for i in range(N-1, -1, -1):
#     for j in range(i):
#         temp1 = numbers[j]
#         temp2 = numbers[j+1]
#         if numbers[j] > numbers[j+1]:
#             numbers[j] = temp2
#             numbers[j+1] = temp1
# for number in numbers:
#     print(number, end="\n")