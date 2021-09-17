croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
a = input()
for i in croatia:
  if i in a:
    a = a.replace(i,"a")
print(len(a))
