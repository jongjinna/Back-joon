N = int(input())
lst = list(map(int, input().split()))
for i in range(N-1):
  a, b = lst[0], lst[i+1]
  while b!=0:
    a = a%b
    a, b = b, a
  print("{}/{}".format(int(lst[0]/a),int(lst[i+1]/a)))