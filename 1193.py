t, sums = 1, 1
num = int(input())
while sums < num:
  t += 1
  sums += t
if t%2 == 1:
  print("{}/{}".format((sums - num + 1),(t-(sums-num))))
else:
  print("{}/{}".format((t-(sums-num)),(sums - num + 1)))