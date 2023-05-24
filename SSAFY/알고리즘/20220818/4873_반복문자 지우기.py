T = int(input())
for test_case in range(1, T + 1):
    char = input()
    char_stack = []
    for i in char:
        if char_stack and i == char_stack[-1]: # char_stack != [] 이거나 i랑 char_stack의 마지막 요소가 같으면
            char_stack.pop() # pop하겠다.
        else: # char_stack == [] or i != char_stack[-1]
            char_stack.append(i) # char_stack
    print(f'#{test_case} {len(char_stack)}')