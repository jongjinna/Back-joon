import sys
t = int(input())
for i in range(t):
  lst = []
  a = 0
  lst = list(map(int, sys.stdin.readline().split()))
  mean = sum(lst[1:])/lst[0]
  for j in range(1, len(lst)):
    if lst[j] > mean:
      a +=1/lst[0]*100
  print('{:.3f}%'.format(a))