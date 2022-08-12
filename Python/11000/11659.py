import sys
N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
sumlst = [0]
for i in range(0, N):
  sumlst.append(sumlst[i]+lst[i])

for _ in range(M):
  a, b = map(int, sys.stdin.readline().split())
  print(sumlst[b]-sumlst[a-1])