score=0
for i in range(int(input())):
  a = input()
  if score < a.count("for") + a.count("while"):
    score = a.count("for") + a.count("while")
print(score)   
