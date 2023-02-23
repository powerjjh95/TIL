import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    Ci_store = ''
    for i in range(N):
        Ci, Ni = map(str, input().split())
        Ni_int = int(Ni)
        Ci_store += Ci * Ni_int

    print(f'#{t}')
    for j in range(0, len(Ci_store), 10):
        print(Ci_store[j : j + 10])