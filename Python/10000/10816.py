import sys
input = sys.stdin.readline

_ = int(input())
N = map(int, (input().split()))
_ = int(input())
M = map(int, (input().split()))
d = {}
for n in N:
  if n in d:
    d[n] += 1
  else:
    d[n] = 1

print(' '.join(str(d[m]) if m in d else "0" for m in M))