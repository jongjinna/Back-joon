import sys
input = sys.stdin.readline
N = int(input())
X = list(map(int, input().split()))

X2 = sorted(list(set(X)))
dic = {X2[i]: i for i in range(len(X2))}
for i in X:
  print(dic[i], end=' ')
