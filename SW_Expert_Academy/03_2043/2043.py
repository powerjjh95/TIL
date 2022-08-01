P, K = map(int, input().split()) 
count = 0 # 시행의 횟수
for i in range(K, P + 1): # K = 100, P = 123 # 즉, range (100, 124) 
    count += 1 # count를 1 씩 증가시킨다.
    if i == P:
        print(count)

# map
## map과 list
### map은 리스트의 요소를 지정된 함수로 처리해주는 함수
### list(map(<func>, <list>))
#### example
ex1 = [1.2, 2.5, 3.7, 4.6]
ex1 = list(map(int, ex1))
print(ex1) # [1, 2, 3, 4]

ex2 = list(map(str, range(10)))
print(ex2) # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print(type(range(10))) # <class 'range'>

ex3 = list(map(str, 'abc'))
print(ex3) # ['a', 'b', 'c']

# input().split()과 map
## <str>.split(<sep>, <maxaplit>) ## <str> : 문자열 / <sep> : 구분자 / maxsplit : 분할횟수
### example
ex4 = "abcde"
print(ex4) # abcde
print(ex4.split()) # ['abcde']

ex5 = "a b c d e"
print(ex5) # a b c d e
print(ex5.split()) # ['a', 'b', 'c', 'd', 'e']
print(ex5.split(',')) # ['a b c d e']

ex6 = "aa.bb.cc.dd.ee"
print(ex6) # aa.bb.cc.dd.ee
print(ex6.split()) # ['aa.bb.cc.dd.ee']
print(ex6.split(",")) # ['aa.bb.cc.dd.ee'] # 문자열에 ,(comma) 가 없기 떄문에 위와 동일하게 출력됨
print(ex6.split(".")) # ['aa', 'bb', 'cc', 'dd', 'ee']
print(ex6.split(".", 3)) # ['aa', 'bb', 'cc', 'dd.ee']