import sys
lst = []
def push(lst, x):
  lst.append(x)
  return lst
def pop(lst):
  if len(lst) == 0:
    return -1
  else:
    return lst.pop()
def size(lst):
  return len(lst)
def empty(lst):
  if len(lst) == 0:
    return 1
  else:
    return 0
def top(lst):
  if len(lst) == 0:
    return -1
  else:
    return(lst[-1])

for _ in range(int(input())):
  input_split = sys.stdin.readline().rstrip().split()
  order = input_split[0]
  if order == "push":
    push(lst, input_split[1])
  elif order == "pop":
    print(pop(lst))
  elif order == "size":
    print(size(lst))
  elif order == "empty":
    print(empty(lst))
  elif order == "top":
    print(top(lst))
