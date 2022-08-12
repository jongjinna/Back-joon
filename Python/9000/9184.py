# import sys
# def w(a,b,c):
#   if a <= 0 or b <= 0 or c <= 0:
#     return 1

#   if a > 20 or b > 20 or c > 20:
#     return w(20, 20, 20)

#   if a < b and b < c:
#     return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

#   else:
#     return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

# def ww(a, b, c):
#   if a <= 0 or b <= 0 or c <= 0:
#     return 1

#   if a <= b or a <= c:
#     return 2**a

#   else:
#     return 2**max(b, c) + 2**(b+c-1) - 1

# while 1:
#   a, b, c = map(int, sys.stdin.readline().split())
#   if a == -1 and b == -1 and c == -1:
#     break
#   # print("ww({}, {}, {}) = {}".format(a, b, c, ww(a,b,c)))
#   print("w({}, {}, {}) = {}".format(a, b, c, w(a,b,c)))

import sys

input = sys.stdin.readline

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if dp[a][b][c]:
        return dp[a][b][c]
    if a < b < c:
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return dp[a][b][c]
    dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    return dp[a][b][c]

dp = [[[0] * (21) for _ in range(21)] for _ in range(21)]
while 1:
  a, b, c = map(int, input().split())
  if a == -1 and b == -1 and c == -1:
      break
  print("w({}, {}, {}) = {}".format(a, b, c, w(a,b,c)))
