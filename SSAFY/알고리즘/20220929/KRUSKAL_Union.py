'''
Make-Set(x)
Find-Set(x)
Union(x, y)
'''

def make_set(x):
    p[x] = x

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x]) # path compression # Find-Set을 행하는 과정에서 만나는 모든 노드들이 직접 root를 가리키도록 포인터를 바꾸어 준다.
    return p[x]

def union(x, y): # rank가 고려 안 된 union
    p[find_set(y)] = find_set(x)

T = int(input())
for t in range(1, T + 1):
    V, E= map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    edges.sort(key=lambda x: x[2]) # 가중치 오름차순 정렬
    p = [0] * (V+1) # 0 ~ V번까지 있으니깐 V+1개
    for i in range(V + 1):
        make_set(i) # list(range(V+1))과 같음

    answer = 0 # 가중치 합산 모아줄 변수
    cnt = 0 # 간선 선택 횟수
    for x, y, w in edges: # 대표자 같으면 다음으로 걍 넘어감
        if find_set(x) != find_set(y): # 대표자가 다른경우에만
            union(x, y)
            answer += w
            cnt += 1

        if cnt == V:
            break

    print(f'#{t} {answer}')