import math
N, K = map(int, input().split())
print(int(math.factorial(N)//(math.factorial(K)*math.factorial(N-K))%10007))