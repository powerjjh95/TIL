answer = []
for index in range(0, 10):
    N = int(input())
    remainder = N % 42
    answer += [remainder]

print(len(set(answer)))

