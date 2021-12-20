import sys
a, b, c = map(int, sys.stdin.readline().split())
count = (c - b) / (a - b)
if count == int(count):
  print(int(count))
else:
  print(int(count)+1)