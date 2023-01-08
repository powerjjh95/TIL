import sys
sys.stdin = open("ex_001_input.txt")

# number = format(int(input()), '.2f')
number = int(input())

inch = 2.54

answer = number * inch

print(f'{number}.00 inch => {answer} cm')
