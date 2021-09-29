N = int(input())
t = 1
for i in range(1,N+1):
  t*=i
count = 0
for i in str(t)[::-1]:
  if i == '0':
    count += 1
  else:
    break
print(count)
