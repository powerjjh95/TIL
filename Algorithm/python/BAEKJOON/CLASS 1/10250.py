# TRY 2
T = int(input())
for t in range(T):
    H, W, N = map(int, input().split(" "))

    room_list = []

    for w in range(1, W + 1):
        for h in range(1, H + 1):
            room_list += [h * 100 + w]
    answer = room_list[N - 1]
    print(answer)

# # TRY 1
# T = int(input())
# for t in range(T):
#     H, W, N = map(int, input().split(" "))
#
#    room_list = []
#    for w in range(1, W + 1):
#        for h in range(1, H + 1):
#            room_list += [str(h) + str(w).zfill(len(str(W)))]
#
#    answer = int(room_list[N-1])
#    print(answer)
# # 다음과 같이 진행하면 W의 길이가 1인 경우 11과 같이 출력