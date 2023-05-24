# 최대힙

def enq(n):
    global last
    last += 1 # 마지막 정점 추가
    heap[last] = n # 마지막 정점에 key 추가
    # 부모가 있고, 부모 < 자식 인경우 자리 교환
    c = last
    p = c // 2 # 완전이진트리에서 부모 정점 번호
    while p and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

def deq():
    global last
    tmp = heap[1] # 루트 백업
    heap[1] = heap[last] # 삭제할 노드의 키를 루트에 복사
    last -= 1
    p = 1
    c = p * 2
    while c <= last:
        if c + 1 <= last and heap[c] < heap[c + 1]: # 오른쪽 자식도 있고, 오른쪽 자식이 더 크면
            c += 1
        if heap[p] < heap[c]: # 자식이 더 크면 최대힙 규칙에 어긋나므로
            heap[p], heap[c] = heap[c], heap[p]
            p = c # 자식을 새로운 부모로
            c = p * 2 # 왼쪽 자식 번호를 계산
        else: # 부모가 더 크면
            break # 비교 중단,
    return tmp

heap = [0] * 100
last = 0

enq(2)
enq(5)
enq(7)
enq(3)
enq(4)
enq(6)
# print()
while last:
    print(deq())