import sys
sys.stdin = open('input.txt')

T = 10
for t in range(1, T + 1):
    input()
    maze = [list(map(int, input().split())) for _ in range(16)]
    print(maze)