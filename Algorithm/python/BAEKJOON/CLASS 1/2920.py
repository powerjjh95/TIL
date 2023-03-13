scale_list = list(map(int, input().split()))

index_list = []
for index in range(1, len(scale_list) + 1):
    index_list.append(index)
    if scale_list == index_list:
        answer = "ascending"
    elif scale_list == index_list[::-1]:
        answer = "descending"
    else:
        answer = "mixed"
print(answer)