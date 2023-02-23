N = int(input())

ans = 0

# # 방법 2
# if N % 4 == 0 and N % 100 != 0 or N % 400 == 0:
#     ans = 1

# 방법1
if N % 4 == 0 and N % 100 != 0:
    ans = 1
elif N % 400 == 0:
    ans = 1

print(ans)
