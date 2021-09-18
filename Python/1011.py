def cal(n):
  a, t = 0, 0
  while n > t:
    a += 2
    t += a
  if t-(a/2) < n:
    print(a)
  else:
    print(a-1)
for i in range(int(input())):
  a, b = map(int, input().split())
  cal(b-a)