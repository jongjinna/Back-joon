def line(a, b):
  res = 1
  for i in range(b-a+1, b+1):
    res *= i
  for i in range(1, a+1):
    res //= i
  return res
for _ in range(int(input())):
  a, b = map(int, input().split())
  print(line(a, b))