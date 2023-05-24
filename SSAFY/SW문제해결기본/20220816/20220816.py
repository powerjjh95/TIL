# 7 8  # Vertex = 7개, Edge = 8개인 그래프가 있을 때,
# 1 2  # 다음 8개의 줄에 연결 정보를 제공
# 1 3
# 2 4
# 2 5  # 2번과 5번이 양방향으로 연결되어 있음!
# 4 6
# 5 6
# 6 7
# 3 7

'''
# # 스택 + 인접 행렬(공간 복잡도 높으나, 단방향 그래프인 경우 전치로 방향 전환 유리)
#
# V, E = map(int, input().split()) # Vertex, Edge 갯수
#
# adj_matrix = [[0] * (V + 1) for _ in range(V + 1)] # V + 1로 하는 이유는 0번 index부터 시작하는 것이 아닌 1번 index부터 시작하려고
#
# for _ in range(E): # 간선 갯수만큼 돌면서 연결 정보를 받음
#     start, end = map(int, input().split()) # 시작점과 끝점
#     adj_matrix[start][end] = 1
#     adj_matrix[end][start] = 1 # 양방향 그래프이기 때문에 시작 - 끝, 끝 - 시작 둘 다 해준다.
#
# stack = [1]
# visited = []
# # adj_list = [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]
#
# while stack: # 스택이 빌때까지 돌아라!
#     current = stack.pop() # 우선 스택에서 현재 위치 하나 뽑고
#     if current not in visited: # 방문하지 않은 곳이라면,
#         visited.append(current) # 방문했다고 체크해줌
#
#     for destination in range(V + 1): # current 입장에서 어디로 갈 수 있는지 모조리 체크
#         # if adj_matrix[current][destination] == 1 and destination not in visited: 도 가능
#         if adj_matrix[current][destination] and destination not in visited: # 갈 수 있거나 and 방문 안했으면
#             stack.append(destination) # 다음 갈 곳으로 Stack에 저장
#
# print('이동경로:', *visited) # 이동경로: 1 3 7 6 5 2 4
'''

'''
# 스택 + 인접 리스트(공간 복잡도 낮음)
V, E = map(int, input().split()) # Vertex, Edge 갯수

adj_list = [[] for _ in range(V + 1)] # 인접리스트 기본틀

# print(adj_list)

for _ in range(E): # 간선 갯수만큼 돌면서 연결 정보를 받음
    start, end = map(int, input().split()) # 시작점과 끝점
    adj_list[start].append(end)
    adj_list[end].append(start)

# print(adj_list)

stack = []
visited = []

while stack:
    current = stack.pop()
    if current not in visited:
        visited.append(current) # 방문했다고 체크해줌

    for destination in adj_list[visited]:
        if destination not in visited:  # 갈 수 있고 + 방문 안했으면!
            stack.append(destination)   # 다음 갈 곳으로 Stack에 저장
print('이동경로:', *visited)    # 이동경로 : 1 3 7 6 5 2 4
'''

#
def dfs(n):
    if n not in visited: # 우선 visited 없으면 넣어줌
        visited.append(n)

    for destination in range(V + 1):
        if adj_matrix[n][destination] and destination not in visited:
            dfs(destination)

V, E = map(int, input().split())

adj_matrix = [[0] * (V + 1) for _ in range(V + 1)] # 인접행렬 기본틀

for _ in range(E): # 간선 갯수만큼 돌면서 연결 정보를 받음
    start, end = map(int, input().split()) # 시작점과 끝점
    adj_matrix[start][end] = 1
    adj_matrix[end][start] = 1

visited = []
dfs(1)
print('이동경로:' *visited) # 이동경로 1 2 4 6 5 7 3 => 다름 주의의