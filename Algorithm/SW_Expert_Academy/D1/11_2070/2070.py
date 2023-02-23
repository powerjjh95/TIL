import sys
sys.stdin = open('input.txt')

T = int(input())
ans = -1
for t in range (1, T + 1):
    num1, num2 = map(int, input().split())

    if num1 < num2:
        ans = '<'
    elif num1 == num2:
        ans = '='
    else:
        ans = '>'

    print(f'#{t} {ans}')