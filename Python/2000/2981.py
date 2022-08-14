import sys
from math import gcd 
N = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(N)]
lst.sort()
ans_lst = []
ans = []
for i in range(1, N):
  ans_lst.append(lst[i] - lst[i-1])

prev = ans_lst[0]
for i in range(1, len(ans_lst)):
    prev = gcd(prev, ans_lst[i])

for i in range(2, int((prev)**(0.5)) + 1): #제곱근까지만 탐색
    if prev % i == 0:
        ans.append(i)
        ans.append(prev//i)
ans.append(prev)
ans = list(set(ans)) #중복이 있을수 있으니 제거
ans.sort()
print(*ans)