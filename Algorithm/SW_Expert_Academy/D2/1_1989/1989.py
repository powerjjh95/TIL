import sys
sys.stdin=open('input.txt')

T = int(input())
for t in range(1, T + 1):
    word = input()

    ans = 0
    if word == word[::-1]:
        ans =1

    print(f'#{t} {ans}')