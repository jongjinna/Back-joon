# import sys
# N = int(sys.stdin.readline())
# lst = [i for i in range(1, N+1)]
# a = 0
# for _ in range(N-1):
#   if len(lst)<=a:
#     a %= len(lst)
#   lst.pop(a)
#   a += 1
# print(lst[0])

from collections import deque

N = int(input())
deque = deque([i for i in range(1, N+1)])

while(len(deque) >1):
    deque.popleft()
    move_num = deque.popleft()
    deque.append(move_num)
    
print(deque[0])