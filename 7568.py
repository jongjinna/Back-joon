# 값 받아와서 리스트화 [[x,y],[x,y],[]///]
num = int(input())
lst = []
for i in range(num):
  a = list(map(int, input().split()))
  lst.append(a)

# 덩치 큰사람 리스트 만들어서 집어넣기
rank = []
for i in range(num):
  count = 0
  for j in range(num):
    if lst[i][0] > lst[j][0] and lst[i][1] > lst[j][1]:
      count += 1
  rank.append(count)

# 순위 정하는 로직
rankset = sorted(rank)
rankset.reverse()
rank_ind=[]
for i in rank:
  rank_ind.append(rankset.index(i)+1)
for i in rank_ind:
  print(i, end=" ")