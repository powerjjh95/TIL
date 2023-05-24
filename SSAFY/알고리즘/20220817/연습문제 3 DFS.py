# # try 1 : fail...
# V, E = map(int, input().split())
# depth = list(map(int, input().split()))
#
# adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]
#
# for i in range(len(depth)):
#     if i % 2 == 0:
#         start = depth[i]
#         end = depth[i + 1]
#     else:
#         continue
#     # print(start, end) # 한 행에 다 표현되는 것을 따로 따로 구분된다.
#     adj_matrix[start][end] = 1
#     adj_matrix[end][start] = 1
#
#     stack = [1]
#     visited = []
#
#     while stack: # 기본은 while stack == [] 이 참이 될 때까지
#         current = stack.pop()  # 우선 스택에서 현재 위치 하나 뽑고
#         if current not in visited:  # 방문하지 않은 곳이라면,
#             visited.append(current)  # 방문했다고 체크해줌
#
#         for destination in range(V + 1):  # current 입장에서 어디로 갈 수 있는지 모조리 체크
#             if adj_matrix[current][destination] and destination not in visited:  # 갈수있고 + 방문 안했으면!
#                 stack.append(destination)  # 다음 갈 곳으로 Stack에 저장
#
#     print('이동경로:', *visited)

# try 2

def dfs(n):
    if n not in visited:
        visited.append(n)

    for destination in range(V + 1):
        if adj_matrix[n][destination] and destination not in visited: #
            dfs(destination) # 다음 재귀 깊이로 이동

V, E = map(int, input().split())
depth = list(map(int, input().split()))

adj_matrix = [[0] * (V + 1) for _ in range(V + 1)] # 인접행렬 기본틀 # index와 Vertex 순서를 동일하게 하기 위해

for i in range(len(depth)):
    if i % 2 == 0:
        start = depth[i]
        end = depth[i + 1]
        adj_matrix[start][end] = 1
        adj_matrix[end][start] = 1

visited = []

dfs(1)

print(*visited)