num = int(input())
lst = []
for i in range(num):
  a = list(map(int, input().split()))
  lst.append(a)

for i in lst:
  count = 1
  for j in lst:
    if i[0] < j[0] and i[1] < j[1]:
      count += 1
  print(count, end=" ")