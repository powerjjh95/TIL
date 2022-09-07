import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T + 1):
     num = list(map(int, input().split()))
     sum_num = 0
     average_num = 0
     for i in range(len(num)):
         sum_num += num[i]
         average_num = sum_num / len(num)

     answer = round(average_num)
     print(f'#{t} {answer}')

