def selfnum():
  for i in [1,3,5,7,9]:
    print(i)
  b, t = 0, 0
  while b<=10000:
    print(20+b)
    t += 1
    b = 11*t

selfnum()

# //NOTE왜 다르지 무슨 규칙이 있는거지?
