P, K = map(int, input().split()) # map함수 
count = 0 # 시행의 횟수
for i in range(K, P + 1): # K = 100, P = 123 # 즉, range (100, 124) 
    count += 1 # count를 1 씩 증가시킨다.
    if i == P:
        print(count)