import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for t in range(1, T + 1):
    N, hexa_num = input().split()

    hexa = {'0' : '0000', '1':'0001', '2':'0010', '3':'0011','4':'0100','5':'0101', '6':'0110', '7':'0111','8':'1000','9':'1001','A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
    hexa_ans = []
    for i in hexa_num:
        if i in hexa:
            hexa_ans.append(hexa[i])
    print(f'#{t}', ''.join(hexa_ans))