import sys 
lst = []
for i in range(9):
  n = int(sys.stdin.readline())
  lst.append(n)
minus = sum(lst) - 100

for i in lst:
  if minus - i in lst:
    if minus - i == i:
      print(i)
    continue
  print(i)
