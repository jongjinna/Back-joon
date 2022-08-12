N, M = map(int, input().split())
a = set()
sum = 0
for i in range(N):
  a.add(input())
for i in range(M):
  b = input()
  if b in a:
    sum += 1
print(sum)