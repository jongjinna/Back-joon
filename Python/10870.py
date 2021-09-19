lst = [0, 1]
a = int(input())
for i in range(2,a+1):
  lst.append(lst[i-2]+lst[i-1])
print(lst[a])