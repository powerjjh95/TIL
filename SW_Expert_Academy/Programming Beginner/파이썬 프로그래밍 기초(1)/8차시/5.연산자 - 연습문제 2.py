import sys
sys.stdin = open("ex_002_input.txt")

number = int(input())

lb = 2.2046

answer = format(number * lb, '.2f')

print(f'{number}.00 kg =>  {answer} lb')