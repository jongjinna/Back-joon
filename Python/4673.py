a = set(range(1,10000))
b = set()
for i in a:
  for j in str(i):
    i += int(j)
  b.add(i)
ans = a - b
for i in sorted(ans):
  print(i)