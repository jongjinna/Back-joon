# import sys

# for _ in range(int(sys.stdin.readline())):
#   cnt = 1
#   test = []
#   n = int(sys.stdin.readline())
#   for _ in range(n):
#     t1, t2 = map(int, sys.stdin.readline().split())
#     test.append((t1, t2))
#   test.sort()
#   last = test[0][1]
#   for i in range(1, n):
#     if test[i][1] < last:
#       cnt += 1
#       last = test[i][1]
#   print(cnt)


n = int(input())
ans = []
for _ in range(n):
  m = int(input())
  a = []
  for _ in range(m):
    a.append(list(map(int, input().split())))
  a.sort(reverse = True)
  print(a)
  b = [1] * m
  t = 1
  if m > 1:
    for i in range(1, m):
      for j in range(i):
        if a[j][1] < a[i][1] and b[j] + 1 > b[i]:
          b[i] = b[j] + 1
      if b[i] > t:
        t = b[i]
  ans.append(t)
for i in ans:
  print(i)