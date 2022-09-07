A, B = list(map(int, input().split()))
# scissor = 1
# rock = 2
# paper = 3
# scissor(1)-rock(2): rock(2)
# rock(2)-paper(3): paper(3)
# paper(3)-scissor(1): scissor(1)

# A가 이기는 경우
if A == 2 and B == 1:
    print('A')
elif A == 3 and B == 2:
    print('A')
elif A == 1 and B == 3:
    print('A')
# B가 이기는 경우
if B == 2 and A == 1:
    print('B')
elif B == 3 and A == 2:
    print('B')
elif B == 1 and A == 3:
    print('B')