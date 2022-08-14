import sys
lst = []
N = int(sys.stdin.readline())
sa, sb = map(int, sys.stdin.readline().split())
lst.append((sa, sb))
for _ in range(N-1):
  a, b = map(int, sys.stdin.readline().split())
  lst.append((a, b))
lst.append((sa, sb))
sum = 0
for i in range(1,N+1):
  sum += lst[i-1][0] * lst[i][1] - lst[i-1][1] * lst[i][0]

print(abs(round(sum/2,1)))