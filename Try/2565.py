import sys
lst = []
for i in range(int(input())):
  a, b = map(int, sys.stdin.readline().split())
  lst.append((a, b))
lst.sort(key = lambda x: x[0])
print(lst)

# 최장 증가 수열 체크해야돼!