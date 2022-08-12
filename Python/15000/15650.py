N, M = map(int, input().split())
lst = []

def dfs():
  if len(lst)==M:
    print(' '.join(map(str,lst)))
    return
    
  for i in range(1,N+1):
    if i not in lst:
      if len(lst)==0:
        lst.append(i)
        dfs()
        lst.pop()
      else:
        x = lst[-1]
        if x < i:
          lst.append(i)
          dfs()
          lst.pop()

dfs()