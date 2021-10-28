import sys
N, K = map(int, sys.stdin.readline().split())
lst = []
for _ in range(N):
  lst.append(int(sys.stdin.readline()))
t = 0
for i in range(N-1, -1, -1):
  if K == 0:
    break
  if lst[i]>K:
    continue
  t += K//lst[i]
  K = K%lst[i]
print(t)