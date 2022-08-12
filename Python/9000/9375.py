import sys
clothes = {}
for _ in range(int(input())):
  clothes.clear()
  ans = 1
  for _ in range(int(input())):
    a, b = map(str, sys.stdin.readline().split())
    if b in clothes:
      clothes[b] += 1
    else:
      clothes[b] = 2
  for i in clothes:
    ans *= clothes[i]
  print(ans - 1)
