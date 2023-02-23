numbers =list(map(int, input().split()))

answer = 0
for i in numbers:
    temp = i ** 2
    answer += temp

print(answer % 10)

