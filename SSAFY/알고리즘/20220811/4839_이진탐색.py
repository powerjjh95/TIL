# 함수도 생각해 보자.
def search(P, target):

    l, r = 1, P # l : 검색 구간 왼쪽, r : 검색 구간 오른쪽, 초기 검색구간 오른쪽은 끝 페이지과 동일
    cnt = 0 # 시행 횟수도 필요하다. 왜냐하면 더 적은 시행을 시행했을 경우를 선별해야하기 때문에
    # print(l, r, c, cnt)
    while l <= r: # while 문은 조건문이 참일 동안 반복해서 시행된다.
        c = (l + r) // 2    # c는 중간페이지
        cnt += 1
        if target < c:
            r = c
        elif target > c:
            l = c
        else: # target == c
            break
    return cnt

T = int(input())
for test_case in range(1, T + 1):
    P, Pa, Pb = list(map(int, input().split())) # P : 전체 쪽 수, Pa : A가 찾아야할 쪽수, Pb: B가 찾아야할 쪽수

    if search(P, Pa) < search(P, Pb):
        ans = 'A'
    elif search(P, Pa) > search(P, Pb):
        ans = 'B'
    else:
        ans = '0'

    print(f'#{test_case} {ans}')