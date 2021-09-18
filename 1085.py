x, y, w, h = map(int, input().split())
if w-x > x:
  a = x
elif w-x == 0 and w-x == w:
  a = 0
else:
  a = w-x
if h-y > y:
  b = y
elif h-y == 0 and h-y == w:
  b = 0
else:
  b = h-y
print(min(a,b))