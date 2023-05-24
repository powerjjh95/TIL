import sys
sys.stdin = open('sample_input.txt')

def merge_sort(input_list):

    if len(input_list) == 1:
        return input_list

    mid = len(input_list) // 2
    left_half = input_list[:mid]
    right_half = input_list[mid:]
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def merge(left, right): # 합치는 애
    result = [0] * (len(left) + len(right))
    l = r = idx = 0

    while l < len(left) <= right[r]:


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    merge = [list(map(int,input())) for _ in range(N)]

