import sys
lst = []
for _ in range(int(input())):
  x, y = map(int, sys.stdin.readline().split())
  lst.append((y,x))
for i in sorted(lst):
  print(i[1], i[0])
