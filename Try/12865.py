import sys

N, M = map(int, sys.stdin.readline().split())
bag = []
for _ in range(N):
  weight, value = map(int, sys.stdin.readline().split())
  bag.append([weight, value, value/weight])

sum_w = 0
sum_v = 0
bag.sort(key= lambda x: x[2], reverse=True)
for i in range(N):
  if bag[i][0] <= M - sum_w:
    sum_w += bag[i][0]
    sum_v += bag[i][1]

  else:
    break
print(sum_v)

# 그리디 말고 다이마믹으로