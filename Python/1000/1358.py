def circle_area(x, y, px, py, r):
  return (px-x)**2 + (py-y)**2 <= r**2

W, H, X, Y, P = map(int, input().split())
radius = H / 2
ans = 0
for _ in range(P):
  a, b = map(int, input().split())
  c1 = circle_area(X, Y+radius, a, b, radius)
  c2 = circle_area(X+W, Y+radius, a, b, radius)
  r1 = X<=a<=X+W and Y<=b<=Y+H
  if c1 or c2 or r1:
    ans += 1
print(ans)