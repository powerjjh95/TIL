while True:
    sides = list(map(int, input().split()))
    if sides.count(0) == 3:
        break
    sides.sort()
    def square(number):
        return number ** 2
    if square(sides[0]) + square(sides[1]) == square(sides[2]):
        print("right")
    else:
        print("wrong")