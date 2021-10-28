n = int(input())
def cal(num):
  if 3 <= num:
    for i in range(3, num+1):
      zero.append(zero[i-1]+zero[i-2])
      one.append(one[i-1]+one[i-2])
  print('{} {}'.format(zero[num], one[num]))
for i in range(n):
  zero = [1,0,1]
  one = [0,1,1]
  k = int(input())
  cal(k)