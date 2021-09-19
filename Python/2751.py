import sys
lst = []
for i in range(int(input())):
  lst.append(int(sys.stdin.readline()))

for i in sorted(lst):
  print(i)