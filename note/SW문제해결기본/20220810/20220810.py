# 2차원 배열의 접근
## 열 우선 순회
for j in range(m): # j = 0 # column(열)이 m줄
    for i in range(n): # i = 0, 1, 2 # row(행)가 n줄
        Array[i][j] # (i, j) = (0, 0), (1, 0), (2, 0) 순으로 진행

for i in range(n): # row(행)가 n줄
    for j in range(m): # column(행)이 m줄
        Array[i][j + (m - 1 - 2*j) * (i%2)] # (m - 1 - 2*j) * (i%2)이 왜 필요함?