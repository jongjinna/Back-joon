def fib(n):
  if n == 1 or n == 2:
    return 1
  else:
    return fib(n-1) + fib(n-2)

def fibbonacci(n):
  d = [0] * n
  d[0], d[1] = 1, 1
  for i in range(2, n):
    d[i] = d[i-1] + d[i-2]
  return d[n-1]

n = int(input())
print(fibbonacci(n), n-2)