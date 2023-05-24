# idea
## 먼저 범위를 어떻게 지정해줘야 할지 생각해 보자.
## 합을 구하여 평균을 구해야 한다.


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    flat = list(map(int, input().split())) # 녹색 부분의 왼쪽 상단 좌표 & 오른쪽 하단 좌표
    field = [list(map(int, input().split())) for _ in range(N)]

    # 초록색 부분만 잘라내자
    green_field = [] # 초록색 부분만 담을 빈 list
    for i in range(flat[0], flat[2] + 1): # 왼쪽 시작점 부터 오른쪽 도착점까지
        for j in range(flat[1], flat[3] + 1): # 왼쪽 상단 부터 오른쪽 하단까지
                green_field += [field[i][j]]

    # 이제 합을 구하여 평균을 구하자
    sum = 0
    for k in range(len(green_field)):
        sum += green_field[k] # green_field를 순회하며 합을 구한다.
    avg = sum // len(green_field) # green field의 합과 길이의 몫만 구한다. 문제에서 소수점은 버린다고 표기

    # 평탄화 작업을 하자.
    cnt = 0 # 초기 cnt 값을 0 으로 초기화
    for i in range(len(green_field)): # green_field를 순회하며
        while green_field[i] != avg: # green_field의 i번째 요소가 avg와 같지 않으면
            if green_field[i] > avg: # green_field가 avg보다 클 때
                green_field[i] -= 1 # green_filed의 값을 1씩 감소
                cnt += 1 # cnt 1씩 증가
            elif green_field[i] < avg: # green_field의 i번째 요소가 avg보다 작을 때
                green_field[i] += 1 # green_field의 값을 1씩 증가
                cnt += 1 # cnt 1씩 증가

    print(f'#{test_case} {cnt}')