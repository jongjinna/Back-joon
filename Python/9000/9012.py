def is_VPS(x):
  score = 0
  for i in range(len(x)):
    if x[i] == '(':
      score += 1
    else:
      score -= 1
    if score < 0:
      return "NO"
  if score == 0:
    return "YES"
  else:
    return "NO"
    
for i in range(int(input())):
  print(is_VPS(input()))
