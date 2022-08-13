import sys
min, max = map(int, sys.stdin.readline().split())
a = 1
num_lst = [1 for i in range(min, max+1)]
cnt = 0
i = 2
while i**2 <= max:
  mul = min// i**2
  while i**2 * mul <= max:
    if i**2 * mul - min >= 0:
      num_lst[i**2 * mul - min] = 0
    mul += 1
  i += 1
print(sum(num_lst))