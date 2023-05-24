T = 10
for test_case in range(1, T + 1):
    input()
    search = input()
    word = input()
    count = 0

    for i in range(len(word)-len(search)+1): # 글자수 생각!!!
        if word[i : i+len(search)] == search:
            count += 1

    print(f'#{test_case} {count}')