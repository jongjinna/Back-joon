import sys
N = int(sys.stdin.readline())
sum_list = [[0 for _ in range(N+1)] for _ in range(N+1)]
lst = list(map(int, sys.stdin.readline().split()))
sum_list[0][1] = lst[0]
sum_list[0][2] = lst[0] + lst[1]
for j in range(2, N):
  for i in range(j, N):
    sum_list[i][0]
    sum_list[i+1] = sum_list[i] + lst[i] - lst[i-j]
print(sum_list)