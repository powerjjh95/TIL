import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for t in range(1, T + 1):
    N = float(input())

    float_binary = ''
    while True:
        if len(float_binary) <= 12:
            if N * 2 > 1:
                float_binary += '1'
                N = (N * 2) - 1
            elif N * 2 < 1:
                float_binary += '0'
                N = N * 2
            else:
                float_binary += '1'
                break
        else:
            float_binary = 'overflow'
            break

    print(f'#{t} {float_binary}')

