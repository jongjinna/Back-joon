import sys
for _ in range(int(input())):
  N, T = map(int, sys.stdin.readline().split())
  timelist = list(map(int, sys.stdin.readline().split()))
  roadlist = []
  for i in range(T):
    x, y = map(int, sys.stdin.readline().split())
    roadlist.append((x,y))
  destination = int(input())

  for i in range(T):
    if roadlist[i][0] == destination:
      roadlist = roadlist[:i]
      break

  print(N,T)
  print(timelist)
  print(roadlist)
  print(destination)
