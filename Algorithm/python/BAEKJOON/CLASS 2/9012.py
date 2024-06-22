N = int(input())
answer = ""
for _ in range(N):
    parenthesis_string = []
    for parenthesis in input():
        if parenthesis == "(":
            parenthesis_string.append(parenthesis)
        elif parenthesis == ")":
            if len(parenthesis_string) != 0 and parenthesis_string[-1] == "(":
                parenthesis_string.pop()
            else:
                parenthesis_string.append(parenthesis)
    if len(parenthesis_string) == 0:
        answer = "YES"
    else:
        answer = "NO"
    print(answer)
