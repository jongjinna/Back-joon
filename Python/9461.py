lst = [1,1,1,2,2]
for i in range(5,101):
  lst.append(lst[(i-5)]+lst[(i-1)])
for _ in range(int(input())):
  N = int(input())
  print(lst[N-1])