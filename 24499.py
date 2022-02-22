a, b = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()
print(sum(lst[-b:]))
