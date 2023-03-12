import sys
sys.stdin = open('ex_003_input.txt')

number = int(input())

print("%0.2f ℃ =>  %0.2f ℉" % (number, 32 + number * 1.8))