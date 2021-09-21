import sys
lst = []
for _ in range(int(input())):
  x, y = map(int, sys.stdin.readline().split())
  lst.append((x,y))
for i in sorted(lst):
  print(i[0], i[1])