import sys
sys.stdin = open('sample_input.txt')

for test_case in range(1, int(input())+1):
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))

    # try1
    sorted_numbers = sorted(numbers)
    set_sorted_numbers = list(set(sorted_numbers))
    ans = set_sorted_numbers[K-1]

    print(f'#{test_case} {ans}')