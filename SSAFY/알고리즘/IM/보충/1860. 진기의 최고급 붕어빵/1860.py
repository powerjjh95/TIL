import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())