import sys
n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
start, end = 0, n-1
last = abs(lst[end] + lst[start])
ans_s, ans_e = lst[start], lst[end]
while start < end:
  tmp = lst[end] + lst[start]
  if abs(tmp) < last:
    last = abs(tmp)
    ans_s, ans_e = lst[start], lst[end]
  if tmp == 0:
    break
  elif tmp > 0:
    end -= 1
  else:
    start += 1
print(ans_s, ans_e)