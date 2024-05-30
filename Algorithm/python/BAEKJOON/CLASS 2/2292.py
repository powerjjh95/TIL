N = int(input())
room_address = 1
number = 1
while N > room_address:
    room_address += 6 * number
    number += 1
print(number)