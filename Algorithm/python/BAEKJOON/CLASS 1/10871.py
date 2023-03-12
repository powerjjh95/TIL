N, X = map(int, input().split())
A = list(map(int, input().split()))
answer = []

for i in range(len(A)):
    if A[i] < X:
        answer.append(A[i])
print(*answer)