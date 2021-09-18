def isPrime(num):
  if num == 1:
    return False
  for i in range(2, int(num**(1/2)+1)):
    if num%i == 0:
      return False
  return True

# main
all_list = list(range(2,123456*2))
check = []
for i in all_list:
  if isPrime(i):
    check.append(i)

a = int(input())
while a != 0:
  count = 0
  for i in check:
    if a < i <= 2*a:
      count += 1
  print(count)
  a = int(input())