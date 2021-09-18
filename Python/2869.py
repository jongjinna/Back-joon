import sys
a, b, c = map(int, sys.stdin.readline().split())
x = round((c / (a-b)))
y = (a//(a-b))
z = x - y + 1
print(z)