T = int(input())
for _ in range(T):
    R, S = map(str, input().split())
    each_S = list(map(str, S))
    answer = ""
    for each in each_S:
        answer += each * int(R)
    print(answer)