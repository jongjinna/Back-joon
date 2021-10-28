import sys
a, b = map(int, sys.stdin.readline().split())
c = list(map(int, sys.stdin.readline().split()))
for i in c:
  if i < b:
    print(i, end=' ')