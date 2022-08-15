lst1 = [1]
lst2 = [2, 4, 8, 6]
lst3 = [3, 9, 7, 1]
lst4 = [4, 6]
lst5 = [5]
lst6 = [6]
lst7 = [7, 9, 3, 1]
lst8 = [8, 4, 2, 6]
lst9 = [9,1]

for _ in range(int(input())):
  a, b = map(int, input().split())
  a = a%10
  if a == 1:
    print(lst1[0])
  elif a == 2:
    print(lst2[((b-1)%4)])
  elif a == 3:
    print(lst3[(b-1)%4])
  elif a == 4:
    print(lst4[(b-1)%2])
  elif a == 5:
    print(lst5[0])
  elif a == 6:
    print(lst6[0])
  elif a == 7:
    print(lst7[(b-1)%4])
  elif a == 8:
    print(lst8[(b-1)%4])
  elif a == 9:
    print(lst9[(b-1)%2])
  else:
    print(10)