# import sys
# sys.stdin = open('input.txt')
#
# T = 10
# for t in range(1, T + 1):
#     for _ in range(16):
#

'''
7 8
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7
'''

V, E = map(int, input().split())
adj_matrix1 = [[0] * (V + 1) for _ in range(V + 1)]
for _ in range(V):
    start, end = map(int, input().split())
    adj_matrix1[start][end] = 1
    adj_matrix1[end][start] = 1

# print(adj_matrix1)

def dfs(n):
    if n not in visited:
        visited.append(n)

    for destination in range(V + 1):
        if adj_matrix1[n][destination] and destination not in visited:
            dfs(destination)

visited = []

dfs(1)

print('이동경로 :', *visited)

# stack = [1]
# visited = []
#
# while stack: # stack 이 empty가 될 때까지
#     current = stack.pop() # pop()는 stack의 가장 마지막 원소를 추출
#     if current not in visited: # visited list에 current(int)가 없을 경우
#         visited.append(current) # visited list에 current를 삽입
#
#     for destination in range(V + 1): # 정점을 모두 순회하며 destination을 확인
#         if adj_matrix1[current][destination] and destination not in visited: # adj_matrix1[current][destination]: 다음 값이 0이 아니고 / visited lsit에 destination이 없는 경우
#             stack.append(destination)
#
# print('이동경로 :', *visited)


# adj_matrix2 = [[] for _ in range(V + 1)]
#
# for _ in range(V + 1):
#     start, end = map(int, input().split())
#     adj_matrix2[start].append(end)
#     adj_matrix2[end].append(start)
#
# print(adj_matrix2)
