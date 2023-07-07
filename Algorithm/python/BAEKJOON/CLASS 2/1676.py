N = int(input())

N_factorial = N
for n in range(N - 1, 0, -1):
    N_factorial *= n
N_factorial_string = str(N_factorial)
# print(N_factorial_string)

count = 0
for n_string in range(len(N_factorial_string) - 1, 0, -1):
    # print(N_factorial_string[n_string])
    if N_factorial_string[n_string] == "0":
        count += 1
    else:
        break
print(count)
