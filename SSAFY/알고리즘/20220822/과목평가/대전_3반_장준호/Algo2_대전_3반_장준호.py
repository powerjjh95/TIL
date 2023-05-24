T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)] # 패턴이 들어있는 행렬
    pattern = [list(map(int, input().split())) for _ in range(3)] # 3 X 3 크기에 matrix를 가진 행렬
    # 구조화가 필요하다.
    # matrix 행렬을 3 X 3 으로 쪼갠 모든 케이스와 pattern과 같은 모양이 있는지 비교하자.
    new_matrix = []
    for i in range(N): # 3개씩 묶기 위해
        for j in range(N - 3 +1):
            new_matrix += [new_matrix[i][j]]
        # print(new_matrix)
