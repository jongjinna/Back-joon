N = int(input())
lst = list(map(int, input().split()))
sorted_lst = sorted(lst)
aa = []
for i in range(N):
  aa.append(sorted_lst.index(lst[i]))
  sorted_lst[sorted_lst.index(lst[i])] = -1
print(*aa)