n = int(input())
lst = list(map(int, input().split()))
lst = sorted(lst)
sum_lst = [0] * (n+1)
for i in range(1,n+1):
  sum_lst[i] = sum_lst[i-1] + lst[i-1]
print(sum(sum_lst))