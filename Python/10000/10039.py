sumscore = 0
for i in range(5):
  a = int(input())
  if a < 40:
    sumscore += 40
  else:
    sumscore += a
print(int(sumscore/5))