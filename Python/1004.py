import sys
t = int(input())
for i in range(t):
  s=0
  x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
  n = int(input())
  for j in range(n):
    cx, cy, r = map(int, sys.stdin.readline().split())
    d1, d2 = ((((x1 - cx)**2) + ((y1 - cy)**2))**(1/2)), ((((x2 - cx)**2) + ((y2 - cy)**2))**(1/2)) 
    if (d1 < r) != (d2 < r):
      s += 1
  print(s)