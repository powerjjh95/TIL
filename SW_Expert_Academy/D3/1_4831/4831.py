import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for t in range(1, T + 1):
    K, N, M = list(map(int, input().split()))
    charge = list(map(int, input().split()))

    # try1
    # 1. station을 모든 인자가 0인 리스트를 만들자.
    # 2. station에 charge를 배정
    # 3.
    station = [0] * N
    for i in range()
