N, M = map(int, input().split())
lst = []

def dfs():
  if len(lst) == M:
    print(' '.join(map(str, lst)))
    return
  for i in range(1, N+1):
    if len(lst) == 0:
      lst.append(i)
      dfs()
      lst.pop()
    else:
      if lst[-1] <= i:
        lst.append(i)
        dfs()
        lst.pop()

dfs()