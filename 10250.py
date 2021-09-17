import sys
for i in range(int(input())):
  H, W, N = map(int, sys.stdin.readline().split())
  a = N%H
  if a == 0:
    a = H
    b = N//H
  else:
    b = 1+N//H
  print(a*100+b)