# try1 : clone coding
T = int(input())
for test_case in range(1, T + 1):
    check = input()
    check_stack = []
    ans = 1
    for i in check:
        if i == '{' or i == '(':                    # i가 열린 괄호를 받을 때
            check_stack.append(i)                   # push하고
        if i == '}' or i == ')':                    # 닫힌 괄호를 받을 때
            if check_stack:                         # check_stack == []이면
                empty = check_stack.pop()           # pop 되는 요인들을 empty에 담는다.
            else:                                   # check_stack != [] 이면
                check_stack.append(i)               # check_stack에 i를 담는다.
                break
            if i == '}' and empty == '(':           # i 가 } 이고, empty가 ( 인 예외를 처리
                check_stack.append(i)
                break
            if i == ')' and empty == '{':           # i 기 ) 이고, empty가 { 인 예외를 처리
                check_stack.append(i)
                break

    if check_stack == []:                           # check_stack이 빈 list이면
        ans = 1                                     # 제대로 돌아간 것
    else:                                           # check_stack이 빈 list가 아니면
        ans = 0                                     # 제대로 돌아가지 않은 것

    print(f'#{test_case} {ans}')

# try2