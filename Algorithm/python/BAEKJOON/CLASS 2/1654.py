K, N = map(int, input().split())
K_length_list = []
for _ in range(K):
    K_length = int(input())
    K_length_list += [K_length]

min_length, max_length = 1, max(K_length_list)

while min_length <= max_length: # max _length가 min_length보다 큰 경우 다음 조건문을 실행
    mid_length = (min_length + max_length) // 2
    line_count = 0
    for length in K_length_list:
        line_count += length // mid_length

    if line_count >= N: # line_count가 N보다 크거나 같으면
        min_length = mid_length + 1 # min_length의 값을 mid_length + 1로 갱신하며 다시 mid_length를 구한다.
    else: # line_count가 N보다 작으면
        max_length = mid_length - 1 # max_length의 값을 mid_length - 1로 갱신하며 다시 max_length를 구한다.
print(max_length)