lst = []
minus = list(input().split("-"))
for i in minus:
    lst.append(i.split("+"))

n = 0
for i in lst[0]:
  n += int(i) *2

for i in lst:
  a=0
  for j in i:
    a += int(j)
  n -= a

print(n)
