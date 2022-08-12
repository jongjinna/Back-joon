a = input()
S = set()
for i in range(len(a)):
  for j in range(len(a)+1):
    if i < j:
      S.add(a[i:j])

print(len(S))

# for i in range(len(a)):
#   for j in range(i, len(a)+1):
# 이런식으로 제한줘도 될 듯
# 시간초과 뜰 줄 알았는데,,