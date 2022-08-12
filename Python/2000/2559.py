import sys
n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
ans = sum(lst[0:m])
result = [ans]
for i in range(n-m):
  ans = ans - lst[i] + lst[i+m]
  result.append(ans)

print(max(result))