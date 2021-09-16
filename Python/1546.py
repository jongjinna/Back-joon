import sys
num = int(input())
scores = list(map(int, sys.stdin.readline().split()))
a=0
for i in scores:
  a += i/max(scores)*100/num
print(a)