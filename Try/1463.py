N = int(input())
count = 0
while N != 1:
  if N%3 == 0:
    N = N//3
    count += 1
  elif N%3 == 1 and N%2 == 0:
    # 16이랑 10 차이 확인하기
    N -= 1
    count += 1
  elif N%3 == 2:
    if N%2 == 0:
      N = N//2
      count += 1
    else:
      N -= 2
      count += 2
print(count)