N = int(input())
A = set(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
B2 = set(B)

Subtractset = B2-A
for i in range(len(B)):
  if B[i] in Subtractset:
    B[i] = 0
  else:
    B[i] = 1

print(*B, sep=" ")