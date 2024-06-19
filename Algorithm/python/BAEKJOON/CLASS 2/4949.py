# TRY 1
'''
- string의 종료가 "."으로 결정된다는 것의 표현이 어려웠음
- bracket_list의 조건(길이가 0이 아니고, character가 닫히는 괄호이다)을 충족시키는 코드의 표현 어려움
'''
while True:
    string = input()
    if string == ".":
        break
    bracket_list = []
    for character in string:
        if character == "(" or character == "[":
            bracket_list.append(character)
        elif character == ")":
            if len(bracket_list) != 0 and bracket_list[-1] == "(":
                bracket_list.pop()
            else:
                bracket_list.append(character)
        elif character == "]":
            if len(bracket_list) != 0 and bracket_list[-1] == "[" :
                bracket_list.pop()
            else:
                bracket_list.append(character)
    if len(bracket_list) == 0:
        print("yes")
    else:
        print("no")
