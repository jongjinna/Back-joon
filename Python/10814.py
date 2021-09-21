import sys
lst = []
for i in range(int(input())):
  age, name = map(str, sys.stdin.readline().split())
  lst.append((int(age), i, name))

for i in sorted(lst):
  print(i[0], i[2])