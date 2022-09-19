import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for t in range(1, T + 1):
    K, N, M = list(map(int, input().split())) # K : 이동 가능, N : 정류장 수, M : 충전기가 설치된 수
    charge = list(map(int, input().split()))

    # try1
    # 1. station을 모든 인자가 0인 리스트를 만들자.
    # 2. station에 charge를 배정
    # 3. charge의 0번째 index를
    station = [0] * (N + 1) # 0번째 정류장도 존재하기 때문에
    charge_count = 0
    for i in range(N + 1):
        for j in charge: #
            station[j] = 1 # station에 충전소 정보 반영, 충전소 : 1
        if station[i] == 1:
