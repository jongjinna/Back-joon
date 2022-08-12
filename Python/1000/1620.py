import sys
input = sys.stdin.readline

N, M = map(int, input().split())
PokemonDict = {}
for i in range(1, N+1):
  P = input().rstrip()
  PokemonDict[i] = P
  PokemonDict[P] = i
for _ in range(M):
    P = input().rstrip()
    if P.isdigit() == True:
      print(PokemonDict[int(P)])
    else:
      print(PokemonDict[P])
