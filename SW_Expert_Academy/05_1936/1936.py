A, B = list(map(int, input().split()))
# scissor = 1
# rock = 2
# paper = 3
# scissor(1)-rock(2): rock(2)
# rock(2)-paper(3): paper(3)
# paper(3)-scissor(1): scissor(1)

if A == 1 and B == 2:
    print(A)
elif A ==