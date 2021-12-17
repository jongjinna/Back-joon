import sys
N = int(input())
lst = []
for _ in range(int(input())):
  a, b = map(int, sys.stdin.readline().split())
  lst.append((a,b))
virus = [1]
for i, j in lst:
  if i in virus:
    virus.append(j)

print(len(set(virus))-1)