x, y, w, h = map(int, input().split())

min_width = 0
max_width = w
min_height = 0
max_height = h

answer = min(x, max_width-x, y, max_height-y)

print(answer)