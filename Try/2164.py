def card(lst):
  lst.pop(0)
  lst.append(lst.pop(0))
  return lst


lst = [i+1 for i in range(int(input()))]
while len(lst) > 1:
  card(lst)
print(lst[0])

# deque 
# import collections 