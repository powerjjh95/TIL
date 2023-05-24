matrix = list(map(int, input().split()))
check = [0] * len(matrix)

def powerset(index):
    if index == len(matrix):
        result = []
        for i in range(len(matrix)):
            if check[i] == 1:
                result.append(matrix[i])
        print(result)
        return

    check[index] = 0
    powerset(index + 1)

    check[index] = 1
    powerset(index + 1)

powerset(0)
if


