t = int(input())
for i in range(t):
  score = 0
  count = 0
  x = input()
  for j in range(len(x)):
    if x[j] == 'O':
      count += 1
      score += count
    else:
      count = 0
  print(score)