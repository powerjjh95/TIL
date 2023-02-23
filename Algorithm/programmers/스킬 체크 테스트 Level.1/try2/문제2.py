# def solution(s, n):
#     answer = ''
#     return answer

Large = []
for i in range(65, 91):
    Large.append(chr(i))
# print(Large)

small = []
for i in range(97, 123):
    small.append(chr(i))
# print(small)

s = input()
n = int(input())
answer = []
for i in s:
    answer += chr(ord(i) + n)
print(answer)
