N = int(input())
b = 0
for i in range(1, N):
  a = i
  for j in str(i):
    a += int(j)
  if a == N:
    b = i
    break
print(b)