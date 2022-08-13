N, K = map(int, input().split())
lst = [i for i in range(1, N+1)]
ans = []
num = 0
for i in range(N):
  num += K-1
  if num >= len(lst):
    num = num%len(lst)
  ans.append(lst.pop(num))
print("<", end="")
print(*ans, sep=', ', end='')
print(">")