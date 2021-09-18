for i in range(int(input())):
  k = int(input())
  n = int(input())
  lst = list(range(1,n+1))
  if n == 1:
    print(1)
  else:
    for j in range(1,k+1):
      for t in range(1, n):
        lst[t] += lst[t-1]
    print(lst[n-1])