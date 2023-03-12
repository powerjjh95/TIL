N = int(input())
for count in range(1, N+1):
    line = ' ' * (N-count) + '*' * count
    print(line)
