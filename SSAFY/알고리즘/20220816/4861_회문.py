T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    table = [input() for _ in range(N)]
    zipped_table = list(map(list, zip(*table))) # asterrisk(*)을 붙이면 모든 table을 다 검색
    ans = ''
    # 회문에서 r행의 0번째와
    for r in range(N):
        for c in range(N-M+1):
            if table[r][c:c+M] == table[r][c:c+M][::-1]:
                ans = table[r][c:c+M]
                break
            if zipped_table[r][c:c+M] == zipped_table[r][c:c+M][::-1]:
                ans = ''.join(zipped_table[r][c:c+M])
                break

    print(f'#{test_case} {ans}')
