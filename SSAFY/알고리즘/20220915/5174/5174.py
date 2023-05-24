import sys
sys.stdin = open('sample_input.txt')

def preorder(n):
    global subtree_count
    if n:
        subtree_count += 1
        preorder(left_child[n])
        preorder(right_child[n])

T = int(input())
for t in range(1, T + 1):
    E, N = map(int, input().split())
    # print(E, N)
    tree = list(map(int, input().split()))
    V = E + 1
    left_child = [0] * (V + 1)
    right_child = [0] * (V + 1)
    subtree_count = 0

    for i in range(E):
        parent, child = tree[2 * i], tree[2 *  i + 1]
        # print(parent, child)
        if left_child[parent] == 0:
            left_child[parent] = child
        else:
            right_child[parent] = child

    preorder(N)
    print(f'#{t} {subtree_count}')


