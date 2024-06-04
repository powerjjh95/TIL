# TRY 1
T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())

    # apartmemt 0층을 i호실을 i로 채우기 위해 설정
    # 각 층의 i호실이 i로 채워짐
    apartment = [[i+1 for i in range(n)] for j in range(k+1)]
    for j in range(k):
        for i in range(n):
            apartment[j + 1][i] = 0 # 0층을 제외한 나머지 층들의 호수를 0으로 바꿈
            for l in range(i+1): # 각 층의 i호실을 순회하기 위해 설정
                apartment[j+1][i] += apartment[j][l] # 지정된 호실의 인원수 파악위해 i호실까지 더하기

    # print(apartment)
    print(apartment[k][n-1])

