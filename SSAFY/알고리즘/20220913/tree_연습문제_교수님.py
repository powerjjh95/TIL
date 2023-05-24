# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

# 전위 순회 => print / 왼 / 오

V = int(input()) # V: vertex(정점), node : 정점
edges = list(map(int, input().split()))
left = [0]*(V+1)
right = [0]*(V+1)
find_root = [0]*(V+1)
root = None

for i in range(V-1):
    parent, child = edges[2*i], edges[2*i+1]
    if not left[parent]:
        left[parent] = child
    else:
        right[parent] = child
    find_root[child] = parent


# print('왼: ', left)
# print('오: ', right)

def preorder(n):
    if n > 0:
        print(n, end=' ')
        preorder(left[n])
        preorder(right[n])

for j in range(1, V+1):
    if find_root[j] == 0:
        root = j
        break

preorder(root)