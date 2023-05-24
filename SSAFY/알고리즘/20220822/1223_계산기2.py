# try1
# 후위표기법을 이용하여 사용해야 함.
#

def cal(problem):
    global problem


for test_case in range(1, 11):
    N = int(input())
    problem = list(map(int, input().split()))
    ans = 0
    for i in range(N):
