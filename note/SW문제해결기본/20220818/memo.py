memo = [0, 1]

def fibo(n):
    # 만약 fibo(2)라고 치면 -> 리스트로 3번째 칸을 생성하고 싶은 것이다. [0, 1, ]
    # 1, n >= 2 : [0, 1]까지는 이미 있으니, 애초에 3칸짜리(인덱스 2) 이상 구하고 싶을때만!
    # 2, n >= len(memo) : [0, 1, 1, 2, 3, 5, 8, ...] 처럼 이미 memo가 꽤 긴 상황을 생각

    if n >= 2 and n >= len(memo):
        memo.append(fibo(n - 1) + fibo(n - 2))
    return memo[n]


print(fibo(4))


def fibo2(n):
    f = [0, 1]

    for i in range(2, n + 1): # 그래서 애초에 3번째 칸(인덱스 3)부터 시작
        f.append(f[i - 1] + f[i - 2])

    return f[n]

print()