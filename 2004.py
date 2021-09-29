import math
n, m = map(int, input().split())
a = math.factorial(n)//(math.factorial(n-m)*math.factorial(m))
cnt = 0
for i in str(a)[::-1]:
  if i == '0':
    cnt += 1
  else:
    break
print(cnt)