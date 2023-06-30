T = int(input())
for t in range(T):
    H, W, N = map(int, input().split(" "))

    room_list = []

    for w in range(1, W + 1):
        for h in range(1, H + 1):
            room_list += [h * 100 + w]
    answer = room_list[N - 1]
    print(answer)
