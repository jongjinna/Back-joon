num = int(input())
t = num
count, temp, newnum = 0, 0, 0
while 1:
  temp = num//10 + num%10
  newnum = (num%10)*10 + temp%10
  count += 1
  num = newnum
  if newnum == t:
    break
print(count)