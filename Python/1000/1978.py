a = int(input())
lst = list(map(int, input().split()))
if 1 in lst:
  lst.remove(1)
c = []
for i in lst:
  for j in range(2,i):
    if i%j == 0:
      c.append(i)
      break
print(len(lst)-len(c))
