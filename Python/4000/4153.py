while 1:
  a, b, c = sorted(list(map(int, input().split())))
  if a == 0 or b == 0 or c == 0:
    break 
  elif c**2 == (a**2) + (b**2):
    print("right")
  else:
    print("wrong")
