# def recursive_power(x, n):
#     if n == 1:
#         return x
#
#     # 짝수 제곱인 경우
#     if not n % 2:
#         y = recursive_power(x, n/2)
#         return y*y
#
#     # 홀수 제곱인 경우
#     else:
#         y = recursive_power(x, (n-1)/2)
#         return y*y*x
#
# print(recursive_power(2, 7))

# # 병합 정렬
# arr = [69, 10, 30, 2, 16, 8, 31, 22]
#
# def merge_sort(input_list): # 쪼개는 애
#
#     if len(input_list) == 1: # 1개 짜리라면 더 쪼갤 필요 없으니깐
#         return input_list # 그대로 다시 return하기
#
#     mid = len(input_list) // 2 # 기준점이 되는 값
#     left_half = input_list[:mid] # 여기서 아이디값 분리
#     right_half = input_list[mid:] # 오른쪽 반
#
#     left = merge_sort(left_half) # 분할정복 재귀호출
#     right = merge_sort(right_half)
#
#     return merge(left,right) # 이미 id값 분리된 얘가 인자로! + 쪼개기가 끝내면 결국 끝은 붙이기 로직
#
# def merge(left, right):
#     result = [0] * (len(left) + len(right)) # 들어갈 틀
#     l = r = idx = 0 # 포인터 3개는 전부 0으로 초기화
#
#     while l < len()

# lomuto
a= [2, 8, 7, 1, 3, 5, 6, 4]

def lomuto(low, high):
    def partition(low, high):
        pivot = a[high]
        ledt = low

    if low < high:
        pivot = partition(low, high)
        lomuto(low, pivot - 1)
        lomuto(pivot + 1, high)

lomuto(1, len(a)-1)
print(a)