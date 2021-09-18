a = int(input())
b = int(input()) 
c = list(range(a, b+1))
d = []
if 1 in c:
  c.remove(1)
for i in c:
  for j in range(2, i):
    if i%j == 0:
      d.append(i)
      break

for i in d:
  c.remove(i)

if len(c) == 0:
  print(-1)
else:
  print(sum(c))
  print(min(c))