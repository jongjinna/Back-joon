a = sorted(input().lower())
lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
count = 0
letter = ""
for i in lst:
  if a.count(i)>count:
    letter = i 
    count = a.count(i)
  elif a.count(i)==count:
    letter = '?'
print(letter.upper())