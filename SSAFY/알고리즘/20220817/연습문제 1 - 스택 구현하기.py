class stack: # stack 클래스 생성
    def __init__(self): # list로 데이터를 담은 바구니를 만든다.
        self.basket = []

    def push(self, data): # stack의 행동은 push와 pop
        self.basket.append(data)

    def pop(self): # 가장 마지막에 들어온 데이터가 가장 먼저 나간다. LIFO(Last-In First_Out)
        return self.basket.pop()

s1 = stack()
s1.push(1)
s1. push('abc')
s1.push([1, 2, 3])
print(s1.pop()) # [1, 2, 3]
print(s1.pop()) # abc
print(s1.pop()) # 1

