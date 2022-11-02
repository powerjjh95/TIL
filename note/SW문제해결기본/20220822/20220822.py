# 재귀함수로 부분집합 구하기
arr = ['A', 'B', 'C']
check = [0, 0, 0]

def powerset(idx):
    if idx == 3:
        print('체크 배열은 다음과 같음: ', *check)
        result = []
        for j in range(3):
            if check[j] == 1:
                result.append(arr[j])
        print(result)
        return

    check[idx] = 0
    powerset(idx + 1)

    check[idx] = 1
    powerset(idx + 1)

    # for i in range(2):
    #   check[idx] = i
    #   powerset(idx + 1)

powerset(0)