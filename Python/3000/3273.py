import sys
n = int(input())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
x = int(input())
count = 0
left, right = 0, n-1
while left < right:
  tmp = lst[left] + lst[right]
  if tmp == x:
    count += 1
  if tmp < x:
    left += 1
    continue
  right -= 1
print(count)