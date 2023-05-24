arr = [2, 4, 1, 3]

for i in range(len(arr)-1, 0, -1): # 역순으로 시행
    print(list(range(len(arr)-1, 0, -1))) # range가 어떻게 생성되는지 궁금해서
    print(list(range(i))) #
    for j in range(i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]