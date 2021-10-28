import sys
t = int(input())
for i in range(t):
  a, b = sys.stdin.readline().split()
  c = ''
  for j in b:
    c += j*int(a)
  print(c)