import sys

N, M = map(int, sys.stdin.readline().split())
bag = {}
for _ in range(N):
  weight, value = map(int, sys.stdin.readline().split())
  bag[weight] = value

print(bag)
