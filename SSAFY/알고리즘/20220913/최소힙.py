# list에 append 된다.
# 삽입과 삭제를 이용하여 문제 해결

'''
6 13 2 7 8 4 11 9
'''

heap = ['최소힙 :']
heap = list(map(int, input().split()))

def heap_push(item):
    heap.append(item) # 완전 이진 트리 형태임으로 마지막에 삽입

    child = len(heap) - 1
    parent = child // 2

    # 루트 노드가 아니고, 위에 봤는데 더 큰 경우 계속 실행
    while parent and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent] # swap
        child = parent
        parent = child // 2

def heap_pop():
    if len(heap) == 1: # 없을 때 뽑지 않는 경우
        return

    result = heap[1]
    item = heap.pop()
    heap[1] = item

    parent = 1
    child = parent * 2

    if child + 1 <= len(heap) - 1:
        if heap[child] > heap[child + 1]:
            child += 1

    # 이번에는 아래로 내려가는거니깐 오른쪽 노드가 존재할때까지 생성
    # 최소힙 유지를 위해 필요할 때까지
    while child <= len(heap) -1 and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child # 이번에는 내려가는 거니깐 반대
        child = parent * 2 # 일단 이번에도 왼쪽이라고 가정해봄

        if child + 1 <= len(heap) - 1:
            if heap[child] > heap[child + 1]:
                child += 1

    return result

heap_push(33)
print(heap)
heap_push(12)
print(heap)
heap_push(7)
heap_push(19)
heap_push(21)
print(heap)
heap_push(5)
print(heap)
heap_push(8)
print(heap)
print(heap_pop())
print(heap)
print(heap_pop())
print(heap)
print(heap_pop())
print(heap)
print(heap_pop())
print(heap)
print(heap_pop())
print(heap)
print(heap_pop())
print(heap)