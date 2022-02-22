n = int(input())
a = 0
lst = list(map(int, input().split(" ")))
for i in range(1, n-1):
  if a < min(lst[i-1], lst[i+1]) + lst[i]:
    a = min(lst[i-1], lst[i+1]) + lst[i]
print(a)
