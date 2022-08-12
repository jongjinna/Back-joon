N = int(input())

grid = []
numlst = []
for _ in range(N):
  grid.append(list(map(int, input().split())))

lst = []
def dfs():
  if len(lst) == 2:
    numlst.append(grid[lst[0]][lst[1]]+ grid[lst[1]][lst[0]])
    return 
  for i in range(0, N):
    if i not in lst:
      if len(lst) == 0:
        lst.append(i)
        dfs()
        lst.pop()
      else:
        if lst[-1] < i:
          lst.append(i)
          dfs()
          lst.pop()
  return numlst
nnn = dfs()
print(nnn)
# 이제 이 점수들 반갈 해서 차이 가장 적게 구하면 되는데,,