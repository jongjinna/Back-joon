import sys
N = int(sys.stdin.readline())

lst= [0,1,0]
a = 2
while a<=N:
  lst[2] = (lst[1] + lst[0])%1000000
  lst[0] = lst[1]
  lst[1] = lst[2]
  a += 1
sys.stdout.write(str(lst[2])+'\n')

# 시간초과나옴 피사노 주기 쓰라는데 몰라