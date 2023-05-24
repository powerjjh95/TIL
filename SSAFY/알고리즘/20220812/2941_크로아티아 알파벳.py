# try1
alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
T = input()

for i in alpha:
    if i in T:
        T = T.replace(i, '*')
# print(T)
print(len(T))