N = int(input())
count = 0
number = 1

# 6이 연속 3개이상 포함
while True:
    if "666" in str(number):
        count += 1

    if count == N:
        print(number)
        break

    number += 1

