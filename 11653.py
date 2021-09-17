a = int(input())
lst = []
if a > 1:
  for i in range(2, a+13):
    while a%i == 0:
      a = a//i
      lst.append(i)
 
  for i in lst:
    print(i)