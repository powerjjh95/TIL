import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())

    quotient = a // b
    remainder = a % b
    print(f'#{test_case} {quotient} {remainder}')