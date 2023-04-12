T = int(input())
for t in range(T):
    OX = input()
    score = 0
    accumulate_score = 0
    for i in range(len(OX)):
        if OX[i] == "O":
            score += 1
            accumulate_score += score
        elif OX[i] == "X":
            score = 0
        # print(t, score, accumulate_score)
    print(accumulate_score)

