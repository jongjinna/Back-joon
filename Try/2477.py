from curses import A_ALTCHARSET


n = int(input())
aa = []
for i in range(6):
  a, b = map(int, input().split())
  aa.append((a, b))
  # if a == 1 or a == 2:
  #   wid.append(b)
  # elif a == 3 or a == 4:
  #   hei.append(b)

print(aa)