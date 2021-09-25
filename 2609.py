def soinsu(n):
  n_lst = []
  for i in lst:
    while 1:
      if n%i == 0:
        n = n//i
        n_lst.append(i)
      else:
        break
  return n_lst


a, b = map(int, input().split())
lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

a_lst = soinsu(a)
b_lst = soinsu(b)
union = list(set(a_lst)|set(b_lst))
intersection = list(set(a_lst)&set(b_lst))
print(intersection)
print(union)