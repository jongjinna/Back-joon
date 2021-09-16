import sys
t = int(input())
for i in range(t):
  x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
  r, rm, rs = (((x1-x2)**2)+((y1-y2)**2))**(1/2), abs(r1-r2), abs(r1+r2)
  if rm < r < rs:
    print(2)
  elif (r == rs) or (r == rm and r !=0): 
    print(1)
  elif r < rm or r > rs:
    print(0)
  else:
    print(-1)