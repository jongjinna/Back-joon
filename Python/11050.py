N, K = map(int, input().split())
t = 1
for i in range(K):
  t *= ((N-i)/(i+1))
print(int(t))