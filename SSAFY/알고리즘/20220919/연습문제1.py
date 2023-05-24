T = int(input())
for t in range(1, T + 1):
    array = list(map(int, input()))

    # try1
    # array를 7개씩 자른다.
    sperate_array = []
    for i in range(0, len(array), 7):
        sperate_array += [array[i:i + 7]]

    # 7개 숫자가 계속 들어오니깐 2**6 ~ 2**0까지 만들어주자.
    binary_list = []
    for i in range(6, -1, -1):
        binary_list += [2 ** i]

    # 이제 곱해서 인덱스를 맞춰 각각의 list에 넣는다.
    ans = []
    for i in range(len(array) // 7):
        temp = 0
        for j in range(7):
            temp += sperate_array[i][j] * binary_list[j]
        ans += [temp]
    print(f'#{t}', *ans)

