import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    tree = list(map(int, input().split()))

    # try2
    # 최소힙을 저장할 트리 초기화
    heap = [0]

    # 최소힙 생성
    for i in range(N):
        heap.append(tree[i])

        child = len(heap) - 1
        parent = child // 2

        while parent and heap[child] < heap[parent]:
            heap[child], heap[parent] = heap[parent], heap[child]

            child = parent
            parent = child // 2

    # 정답 초기화
    sum_node = 0 # sum_node : 조상 node의 합

    # 마지막 노드의 바로 위 부모 노드 번호르 변수에 저장
    parent = (len(heap) - 1) // 2

    while parent:
        sum_node += heap[parent]
        parent = parent //2

    print(f'#{t} {sum_node}')


    # # try1
    # for i in range(N - 1, -1, -1):
    #     if tree[i] > tree[i // 2]:
    #         tree[i], tree[i // 2] = tree[i // 2], tree[i]
    #     elif tree[i] > tree[(i // 2) + 1]:
    #         tree[i], tree[(i // 2) + 1] = tree[(i // 2) + 1], tree[i]
    # print(tree)
