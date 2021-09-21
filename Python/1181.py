lst = set()
for _ in range(int(input())):
  a = input()
  if len(a)<10:
    b = str(0)+str(len(a))
  else:
    b = str(len(a))
  lst.add(b+a)
for i in sorted(list(lst)):
  print(i[2:])