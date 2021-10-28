M, N = map(int, input().split())
Map = []
Min = []
for i in range(M):
  Map.append(input())

for a in range(M - 7):
  for b in range(N - 7):
    idx1 = 0
    idx2 = 0
    for c in range(a, a + 8):
      for d in range(b, b + 8):              
        if (d + c)%2 == 0:
          if Map[c][d] != 'W': idx1 += 1  
          if Map[c][d] != 'B': idx2 += 1
        else :
          if Map[c][d] != 'B': idx1 += 1
          if Map[c][d] != 'W': idx2 += 1
    Min.append(idx1)                          
    Min.append(idx2)                         
print(min(Min))    