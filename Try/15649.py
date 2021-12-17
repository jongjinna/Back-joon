N, M = map(int, input().split())
lst = []
for i in range(1, N+1):
  lst.append(i)

for i in range(M):
  for j in range(N):
    print('나도 모르겠다아아아!')
for i in range(N):
  for j in range(N):
    if i == j:
      continue
    else:
      print(lst[i], lst[j])

# 자 이제 m을 써야되는데.