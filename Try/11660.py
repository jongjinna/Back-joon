import sys
n, m = map(int, sys.stdin.readline().split())
grid = []
for _ in range(n):
  grid.append(list(map(int, sys.stdin.readline().split())))

for _ in range(m):
  sum = 0
  x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
  for i in range(x1-1, x2):
    for j in range(y1-1, y2):
      sum += grid[i][j]
  print(sum)


# 이렇게 해보자
4 3
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7

1 3 6 10
3 9 15 24
6 15 27 42
10 19 42 64



2 2 3 4
3 4 3 4
1 1 4 4
