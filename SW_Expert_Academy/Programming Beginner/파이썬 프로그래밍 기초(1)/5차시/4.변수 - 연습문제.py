import sys
sys.stdin = open("ex_074_input.txt")

a = int(input())

ans = 0
tmep2 = 0
for i in range(0, 4):
    temp = a * (10 ** i)
    tmep2 += temp
    ans += tmep2

print(ans)
