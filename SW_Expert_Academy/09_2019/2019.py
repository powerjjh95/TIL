import sys
sys.stdin = open('input.txt')

# # try2
# T = int(input())
# ans = ''
# for i in range(T + 1):
#     ans += str(2 ** i)
# output_list = ' '.join(ans)
# print(output_list) # 1 2 4 8 1 6 3 2 6 4 1 2 8 2 5 6

# try1 : pass
T = int(input())
ans = []
for i in range(T + 1):
    ans += [str(2 ** i)]
output_list = ' '.join(ans)
print(output_list) # 1 2 4 8 16 32 64 128 256