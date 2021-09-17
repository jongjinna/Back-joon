t = int(input())
c = 0
for i in range(t):
  word = list(input())
  for j in range(len(word)-1):
    if word[j] != word[j+1]:
      try:
        if word[j] in word[j+2:]:
          c-=1
          break
      except:
        print("error")

print(c+t)