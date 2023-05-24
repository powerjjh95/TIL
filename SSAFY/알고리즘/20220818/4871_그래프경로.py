T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        start, end = map(int, input().split())
        adj_matrix[start][end] = 1
    S, G = map(int, input().split())

    stack = [S]
    visited = []
    ans = 0

    while stack: # stack == []일 떄까지
        current = stack.pop() # 우선 스택에서 현재 위치 하나 뽑고
        if current not in visited:
            visited.append(current)
        if current == G:
            ans = 1
            break

        for destination in range(V + 1):
            if adj_matrix[current][destination] and destination not in visited:
                stack.append(destination)

    print(f'#{test_case} {ans}')