N, S = map(int, input().split())
lst = list(map(int, input().split()))
sum_lst = [0] * (N+1)
for i in range(1, N+1):
    sum_lst[i] = sum_lst[i-1] + lst[i-1]
left, right = 0, 1
last_ans = N + 1
while right < N+1:
  if sum_lst[right] - sum_lst[left] >= S:
    if right - left < last_ans:
      last_ans = right - left
    left += 1
  else:
    right += 1
print(last_ans if last_ans != (N + 1) else 0)
