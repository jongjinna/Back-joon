lst = []
N = int(input())
for _ in range(N):
  lst.append(int(input()))

lst = sorted(lst)
a = True
ans = []
for i in range(2,lst[0]+1):
  a = False
  for j in range(1, len(lst)):
    if lst[j]%i != lst[0]%i:
      break
    a = True
  if a:
    ans.append(i)

print(*ans, sep=' ')