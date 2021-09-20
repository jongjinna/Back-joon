def mean(lst):
  return round(sum(lst)/a)

def median(lst):
  if a == 1:
    return lst[0]
  else:
    if a%2 != 0:
      return lst[int(a//2)]
    else:
      return round((lst[a//2]+lst[a//2+1])/2)

def modes(lst):
  from collections import Counter
  if a == 1:
    return lst[0]
  else:
    c = Counter(lst).most_common(2)
    return c[1][0] if c[0][1] == c[1][1] else c[0][0]

def ranges(lst):
  return lst[a-1]-lst[0]

# main
a = int(input())
lst = sorted([int(input())] for _ in range(a))

print(mean(lst))
print(median(lst))
print(modes(lst))
print(ranges(lst))