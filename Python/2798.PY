N, M = map(int, input().split())
num = list(map(int, input().split()))
a = 0
for i in range(N):
  for j in range(i+1,N):
    for k in range(j+1,N):
      if num[i]+num[j]+num[k] > M:
        continue
      else:
        a = max(num[i]+num[j]+num[k], a)
print(a)