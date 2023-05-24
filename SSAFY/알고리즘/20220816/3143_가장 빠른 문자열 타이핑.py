T = int(input())
for test_case in range(1, T + 1):
    A, B = input().split()
    # print(type(A)) # str
    # print(B)

    if B in A:
        A = A.replace(B, '*')

    print(f'#{test_case} {len(A)}')

    # 만약 B가 A안에 있다면 1번 쓰는 거
    # 그렇지 않다고 해도 포함되지 않은 알파벳을 다 세어야 하니깐
    # 먼저 글자 개수 다 구해놓고 거기서 B 빼면 되니깐