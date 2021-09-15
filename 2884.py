a, b = map(int, input().split())
if b < 45:
  if a != 0:
    print(a-1,15+b)
  else:
    print(23, 15+b)
else:
  print(a, b-45)