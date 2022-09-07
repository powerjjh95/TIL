import sys
sys.stdin = open('SampleInput.txt')

# try1과 try2의 차이가 뭘까?
# try2 : pass
N = int(input())
output_list = []
for i in range(N, -1, -1):
    output_list += [str(i)]
# print(output_list) #876543210

ans = ' '.join(output_list)
print(ans) # 8 7 6 5 4 3 2 1 0

# try1 : fail
N = int(input())
output_list = ''
for i in range(N, -1, -1):
    output_list += str(i)
# print(output_list) #876543210

ans = ' '.join(output_list)
print(ans) # 8 7 6 5 4 3 2 1 0
