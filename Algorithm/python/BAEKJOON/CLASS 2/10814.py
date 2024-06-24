# TRY 1
'''
-
'''
N = int(input())
online_judge = []
for _ in range(N):
    age, name = input().split()
    online_judge.append([int(age), name])

online_judge.sort(key=lambda x: x[0])

for member in online_judge:
    print(member[0], member[1])



